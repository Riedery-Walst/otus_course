<h1>Привет!</h1>

<p>Здесь представлен проект по расчитыванию среднего значения от чисел</p>

<pre>
def calculate_average(nums):
    total = sum(nums)
    count = len(nums)
    average = total / count
    return average

nums = [10, 15, 20]
print("Среднее:", calculate_average(nums))</pre>