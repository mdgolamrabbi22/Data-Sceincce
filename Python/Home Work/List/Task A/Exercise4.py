numbers = [0, 5, 0, 3, 8, 0, 2]

pos = 0

for i in range(len(numbers)):
    if numbers[i] != 0:
        numbers[pos] = numbers[i]
        pos += 1

for i in range(pos, len(numbers)):
    numbers[i] = 0

print(numbers)
