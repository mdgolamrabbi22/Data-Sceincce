numbers = [1, 2, 3, 2, 1]
sort_list = []
reverse_list = []

for i in numbers:
    sort_list.append(i)


for i in range(len(numbers)-1, -1, -1):
    reverse_list.append(numbers[i])


if sort_list == reverse_list:
    print("Number is plaindrome.")
else:
    print("Number is not palindrome.")
