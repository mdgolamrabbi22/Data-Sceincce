odd_number = 0
even_number = 0

for i in range(1, 21):
    if i % 2 == 0:
        even_number = even_number + 1
    else:
        odd_number = odd_number + 1


print(f"1-20 Even Number count {even_number}")
print(f"1-20 Odd number count {odd_number}")
