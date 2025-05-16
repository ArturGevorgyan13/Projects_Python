import random

print("Let's play HANGMAN!!!")

print("You have only 6 lives so try to guess the word within 6 attempts! Good luck!!!")

words=["apple","cat","dog","elephant","sun","joker","special","table","classic","computer"]

hangman_stages = [
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |
    --------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |
    --------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |
     |
    --------
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |
     |
    --------
    """,
    """
     ------
     |    |
     |    O
     |    |
     |
     |
    --------
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
    --------
    """,
    """
     ------
     |    |
     |
     |
     |
     |
    --------
    """
]


word=random.choice(words)

guessword=[]

for letter in word:
    guessword+="_"

print(guessword)

lives=6

game_over=False

while not game_over:
    letter=input("Guess a letter: ").lower()

    if letter not in word:
        lives-=1

        if lives!=0:
            print(f"You don't guess the letter, now you have {lives} lives!")
        
        if lives==0:
            game_over=True
            print("You lose!")

    for i in range(len(word)):
        if word[i]==letter:
            guessword[i]=letter

    if "_" not in guessword:
        game_over=True
        print("You win!")

    print(hangman_stages[lives])

    print(guessword)   