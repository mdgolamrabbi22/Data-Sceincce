import math
numbers = [2, 4, 4, 4, 5, 5, 7, 9]
total = 0
sqare_sum = 0

for i in numbers:
    total = total + i
    mean = total / len(numbers)


for i in numbers:
    sub = i - mean
    con = sub ** 2
    sqare_sum = sqare_sum + con


sqared_variance = sqare_sum / len(numbers)
standard_divition = math.sqrt(sqared_variance)
print(standard_divition)
