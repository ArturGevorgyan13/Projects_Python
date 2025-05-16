import random
import os

def choose_singers(singer_followers):
    
    singer1=random.choice(singer_followers)
    
    singer2=random.choice(singer_followers)
    
    while singer1==singer2:
        
        singer2=random.choice(singer_followers)
    
    return singer1,singer2

singer_followers=[
    {"name": "Taylor Swift", "follower_count": 280_000_000, "description": "singer-songwriter", "country": "USA"},
    {"name": "Ariana Grande", "follower_count": 250_000_000, "description": "pop singer and actress", "country": "USA"},
    {"name": "BTS", "follower_count": 210_000_000, "description": "K-pop boy band", "country": "South Korea"},
    {"name": "Selena Gomez", "follower_count": 200_000_000, "description": "singer and actress", "country": "USA"},
    {"name": "Billie Eilish", "follower_count": 180_000_000, "description": "alternative pop singer", "country": "USA"},
    {"name": "Drake", "follower_count": 160_000_000, "description": "rapper and singer", "country": "Canada"},
    {"name": "The Weeknd", "follower_count": 150_000_000, "description": "R&B singer", "country": "Canada"},
    {"name": "Justin Bieber", "follower_count": 240_000_000, "description": "pop singer", "country": "Canada"},
    {"name": "Rihanna", "follower_count": 140_000_000, "description": "singer and entrepreneur", "country": "Barbados"},
    {"name": "Ed Sheeran", "follower_count": 170_000_000, "description": "singer-songwriter", "country": "UK"},
    {"name": "Shakira", "follower_count": 130_000_000, "description": "Latin pop singer", "country": "Colombia"},
    {"name": "Dua Lipa", "follower_count": 120_000_000, "description": "pop singer", "country": "UK"},
    {"name": "Katy Perry", "follower_count": 110_000_000, "description": "pop singer", "country": "USA"},
    {"name": "Lady Gaga", "follower_count": 100_000_000, "description": "singer and actress", "country": "USA"},
    {"name": "BLACKPINK", "follower_count": 190_000_000, "description": "K-pop girl group", "country": "South Korea"},
    {"name": "Bad Bunny", "follower_count": 90_000_000, "description": "reggaeton and trap artist", "country": "Puerto Rico"},
    {"name": "Post Malone", "follower_count": 85_000_000, "description": "rapper and singer", "country": "USA"},
    {"name": "Sia", "follower_count": 75_000_000, "description": "singer-songwriter", "country": "Australia"},
    {"name": "Adele", "follower_count": 95_000_000, "description": "soul/pop singer", "country": "UK"},
    {"name": "Camila Cabello", "follower_count": 88_000_000, "description": "pop singer", "country": "USA"},
]

higher_lower=r"""  
  _    _ _       _               
 | |  | (_)     | |              
 | |__| |_  __ _| |__   ___ _ __ 
 |  __  | |/ _` | '_ \ / _ \ '__|
 | |  | | | (_| | | | |  __/ |   
 |_|  |_|_|\__, |_| |_|\___|_|   
 | |        __/ |                
 | |     __|___/    _____ _ __   
 | |    / _ \ \ /\ / / _ \ '__|  
 | |___| (_) \ V  V /  __/ |     
 |______\___/ \_/\_/ \___|_|     

                                 """

print(higher_lower)

input("Please, enter if you want to start!")

score=0

def game(singer1=None):

    global score

    if singer1==None:

        singer1,singer2=choose_singers(singer_followers)

    else:
        
        singer2=random.choice(singer_followers)

        while singer1==singer2:

            singer2=random.choice(singer_followers)

    info1=f"{singer1["name"]}, a {singer1["description"]} from {singer1["country"]}"

    info2=f"{singer2["name"]}, a {singer2["description"]} from {singer2["country"]}"

    print(f"Compare 1: {info1}")

    print(r""" 
    __      _______ 
    \ \    / / ____|
     \ \  / / (___  
      \ \/ / \___ \ 
       \  /  ____) |
        \/  |_____/ 
                    
                    """)

    print(f"Compare 2: {info2}")

    select=int(input("Who has more followers? Type '1' or '2': "))

    if select==1:

        if singer1["follower_count"]>singer2["follower_count"]:
        
            score+=1
        
            print(f"You are right! Your score is {score}!")
        
            game(singer1)
        
        else:
        
            os.system('clear')
        
            print(higher_lower)
        
            print(f"You are wrong! Your final score is {score}!")

    else:

        if singer1["follower_count"]<singer2["follower_count"]:
        
            score+=1
        
            print(f"You are right! Your score is {score}!")
        
            game(singer2)
        
        else:
        
            os.system('clear')
        
            print(higher_lower)
        
            print(f"You are wrong! Your final score is {score}!")

game()