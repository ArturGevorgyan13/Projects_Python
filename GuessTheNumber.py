import random

EASY_LEVEL=10
HARD_LEVEL=5

def set_difficulty(difficult):
    if difficult=='easy':
        return EASY_LEVEL
    else:
        return HARD_LEVEL

print(r"""
   _____                  _______ _          _   _                 _               
  / ____|                |__   __| |        | \ | |               | |              
 | |  __ _   _  ___  ___ ___| |  | |__   ___|  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __| |  | '_ \ / _ \ . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \ |  | | | |  __/ |\  | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/_|  |_| |_|\___|_| \_|\__,_|_| |_| |_|_.__/ \___|_|                                                                                      
                                                                                   """)

input("Please, enter if you want to start!")

input("Let me think of a number between 1 to 50!")

num=random.randint(1,50)

difficult=input("Choose level of difficulty! Type 'easy' or 'hard': ")

attempt=set_difficulty(difficult)

while attempt!=0:
    print(f"You have {attempt} attempts remaining to guess the number!")
    number=int(input("Make a guess: "))
    if number>num:
        attempt-=1
        print("Your guess is HIGH!")
    elif number<num:
        attempt-=1
        print("Your guess is LOW!")
    else:
        print(f"Your guess is RIGHT! The answer is {num}")
        break
    if attempt==0:
        print("You are out of guesses! You lose!")
        break
    print("Guess again!")