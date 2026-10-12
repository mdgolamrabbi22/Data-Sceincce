numbers = [1, 2, 4, 5, 6]
n = 6

for i in range(1, n+1):
    if i not in numbers:
        missing_value = i

print(f"Missing value is {missing_value}")
