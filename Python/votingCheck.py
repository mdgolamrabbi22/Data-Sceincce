age = int(input("Enter your age."))
citizen = input("You are citizen of Bangladesh. yes?no ")

if citizen.upper() == "YES":
    citizen = True
elif citizen.upper() == "NO":
    citizen = False

if age >= 18 and citizen == True:
    print("You are eligible.")
else :
    print("You are not eligible.")