numbers = [2, 3, 2, 5, 3, 2, 5, 8]
unique_Number = []

for i in numbers:
    if i not in unique_Number:
        unique_Number.append(i)


for i in unique_Number:
    count = 0
    for j in numbers:
        if j == i:
            count = count + 1
    print(f"{i} = {count}")
