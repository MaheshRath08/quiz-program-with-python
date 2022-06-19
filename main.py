print("---Welcome to Our Quiz Game---")
print("---answer the following questions correctly---")

askEm = input("Do you wanna start the game ?(yes to start)").lower()
if askEm != "yes":
    quit()

print("----------------------------------")
print("Lets strat the game...")
score = 0

myAns = input("what is the 11th month of a year?\n").lower()
if myAns == "november":
    print("correct!")
    score+=1
else:
    print("Incorrect!")

myAns = input("What is the capital of England?\n").lower()
if myAns == "london":
    print("correct!")
    score+=1
else:
    print("Incorrect!")

myAns = input("who is the most powerful avenger?\n").lower()
if myAns == "thor":
    print("correct!")
    score+=1
else:
    print("Incorrect!")

myAns = input("what is the hottest country in the world?\n").lower()
if myAns == "mali":
    print("correct!")
    score+=1
else:
    print("Incorrect!")

myAns = input("what is the most populated country in the world?\n").lower()
if myAns == "china":
    print("correct!")
    score+=1
else:
    print("Incorrect!")


print("---------------------------------")
print(f"You scored {score} out of 5")
print(f"You scored {score*100/5}%")
print("---------------------------------")