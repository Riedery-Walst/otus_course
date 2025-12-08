def get_round(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return round(result)
    return wrapper