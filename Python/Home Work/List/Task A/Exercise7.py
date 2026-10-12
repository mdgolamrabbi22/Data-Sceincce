list1 = [1, 2, 3, 4, 3]
list2 = [3, 4, 5, 3, 6]

common_list = []

for i in list1:

    for j in list2:
        if i == j:
            if j not in common_list:
                common_list.append(j)

print(common_list)
