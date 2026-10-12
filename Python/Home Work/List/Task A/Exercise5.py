numbers = [1, 2, 3, 4, 5]
k = 2

first_number = numbers[:-k]
last_number = numbers[-k:]

new_list = last_number + first_number

print(new_list)
