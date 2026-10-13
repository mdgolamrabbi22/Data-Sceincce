numbers = [1, 2, 2, 3, 3, 3, 4]
unique_Number = []
max_count = 0
mode = None

for i in numbers:
    if i not in unique_Number:
        unique_Number.append(i)


for i in unique_Number:
    count = 0
    for j in numbers:
        if j == i:
            count = count + 1
    if max_count < count:
        max_count = count
        mode = i


print(f"Mode is {mode} and count is {max_count}")
