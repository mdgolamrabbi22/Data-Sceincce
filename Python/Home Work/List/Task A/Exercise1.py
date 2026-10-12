data = [12, 45, 7, 45, 32, 19, 32]

number = []
for i in data:
    if i not in number:
        number.append(i)

max_number = number[0]
sec_max = max_number

for i in number:
    if max_number < i:
        sec_max = max_number
        max_number = i
    elif max_number > i and sec_max < i:
        sec_max = i

print(max_number)
print(sec_max)
