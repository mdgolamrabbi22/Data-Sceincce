number = int(input("Enter the Number :"))
how = int(input("How Many Time :"))

for x in range(how):
    numbe = number * x
    x = x + 1
    print(f"{number} * {x} = {numbe}")


    