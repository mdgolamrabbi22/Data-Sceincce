data = [10, 20, 45, 78, 14, 25, 58, 45,]
even_number = []
odd_number = []

for x in data:
    if x % 2 == 0:
        even_number.append(x)
    else:
        odd_number.append(x)

print(f"list in Even number: {even_number}")
print(f"list in Odd number: {odd_number}")
