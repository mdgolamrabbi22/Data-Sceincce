import math
numbers = [10, 11, 12, 10, 11, 100]
total = 0
sqared_sum = 0

for i in numbers:
    total = total + i


mean = total / len(numbers)

for i in numbers:
    sub = mean - i
    con = sub ** 2
    sqared_sum = sqared_sum + con

standard_variance = sqared_sum / len(numbers)
standard_divition = math.sqrt(standard_variance)
print(standard_divition)

check_list = []
for i in numbers:
    if abs(i - mean) <= 2 * standard_divition:
        check_list.append(i)

print(check_list)
