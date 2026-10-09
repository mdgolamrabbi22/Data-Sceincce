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