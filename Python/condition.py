Worker = input("Are You Worker ?yes/no")
card = input("Card Available ? yes/no")

if Worker.upper() == "YES":
    Worker = True
elif Worker.upper() == "NO":
    Worker = False
    
if card.upper() == "YES":
    card = True
elif card.upper() == "NO":
    card = False
    
if Worker == True :
    if card == True:
        print("You are Enter.")
    else:
        print("Your card Unavailable.")
else:
    print("You are Not Worker.")
#Exercise 1

# number = int(input("Enter The value"))

# if number > 0:
#     print("Number is positive.")
# else:
#     print("Number is Negative .")
    

#Exercise 2

# numbers = int(input("Enter The value"))

# if numbers % 2 == 0:
#     print("Number is Even.")
    
# else :
#     print("Number is Odd.")
    

#Exercise 3

age = int(input("Enter your age."))
citizen = input("You are citizen of Bangladesh. yes?no ")

if citizen.upper() == "YES":
    citizen = True
elif citizen.upper() == "NO":
    citizen = False

if age >= 18 and citizen == True:
    print("You are eligible ")
else :
    print("You are not eligible .")
    

#Exercise 4

# a = int(input("Enter the number:"))
# b = int(input("Enter the number:"))

# if a > b:
#     print(f"{a} is max number.")
# else:
#     print(f"{b} is max number.")
    

#Exercise 5

marks = int(input("Enter Your Marks :"))

if marks >= 33 :
    print("You are Passed.")
else:
    print("You are Fail.")
