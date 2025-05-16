import os

def clear_screen():
    os.system('clear')

print("* * * * * * *Welcome to the Silent Auction program!* * * * * * *")

input("Press ENTER to start!")

case="yes"

people={}

while case=="yes":
    if case=="yes":
        clear_screen()

    name=input("What is your name?\n")
    bid=int(input("What is your bid?\n"))

    people[name]=bid

    case=input("Are there any other bidders? Type 'yes' or 'no'!\n").lower()

winner=""

max=0

for person in people:
    if people[person]>max:
        max=people[person]

        winner=person

print(f"Here is the list of bidders!\n{people}")

print(f"The winner is {winner} with a bid of {max}.")