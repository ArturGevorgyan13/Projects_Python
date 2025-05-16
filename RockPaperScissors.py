import random

you=int(input("Please, enter.\n0 for ROCK!\n1 for PAPER!\n2 for SCISSORS!\n"))

computer=random.randint(0,2)

print(computer)

if you==computer:
    print("Draw!")
elif you==computer+1:
    print("You win!")
elif computer==you+1:
    print("You lose!")
elif you==computer+2:
    print("You lose!")
elif computer==you+2:
    print("You win!")
else:
    print("Invalid number!")