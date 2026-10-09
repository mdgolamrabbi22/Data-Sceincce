data = [10, 15, 47, 84, 15, 24, 69]
maxnumber = data[0]

for x in data:
    if maxnumber < x:
        maxnumber = x

print(f"Maxnumber is {maxnumber}")
