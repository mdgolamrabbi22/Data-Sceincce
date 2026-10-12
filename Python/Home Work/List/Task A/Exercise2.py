numbers = [4, 2, 4, 1, 2, 5, 1]
new_list = []
for i in numbers:
    if i not in new_list:
        new_list.append(i)

print(new_list)
