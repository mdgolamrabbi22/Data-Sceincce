numbers = [7, 2, 9, 4, 5, 8, 9]
numbers.sort()

if len(numbers) % 2 != 0:
    length = len(numbers) // 2
    median = numbers[length]
    print(median)
elif len(numbers) % 2 == 0:
    length1 = len(numbers) // 2 - 1
    length2 = len(numbers) // 2
    median = (numbers[length1] + numbers[length2]) / 2
    print(median)
