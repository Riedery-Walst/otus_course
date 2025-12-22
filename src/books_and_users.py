import csv
import json
from itertools import cycle

TO_ROOT = "../"
USERS_PATH = TO_ROOT + "users.json"
BOOKS_PATH = TO_ROOT + "books.csv"
RESULT_PATH = TO_ROOT + "result.json"

USER_KEYS = ("name", "gender", "address", "age")
BOOK_KEYS = ("Title", "Author", "Genre", "Pages")

users = []
with open(USERS_PATH, "r") as f:
    raw_users = json.load(f)
    for user in raw_users:
        users.append({
            key: user.get(key) for key in USER_KEYS
        })

books = []
with open(BOOKS_PATH, "r") as f:
    raw_books = csv.DictReader(f)
    for book in raw_books:
        books.append({
            key.lower(): int(book.get(key)) if book[key].isdigit() else book.get(key)
            for key in BOOK_KEYS
        })

for user in users:
    user["books"] = []

user_cycle = cycle(users)

for book in books:
    user = next(user_cycle)
    user["books"].append(book)

with open(RESULT_PATH, "+w") as f:
    json.dump(users, f, indent=4)