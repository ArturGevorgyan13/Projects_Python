import random

print(list)

print("Welcome to password creator program!")

count_of_letters=int(input("How many letters?"))

count_of_symbols=int(input("How many symbols?"))

count_of_numbers=int(input("How many numbers?"))

symbols=list(range(33,48))+list(range(58,67))+list(range(91,97))+list(range(123,127))

letters=list(range(97,122))+list(range(65,91))

password=[]

for i in range(count_of_letters):
    password.append(chr(random.choice(letters)))

for i in range(count_of_numbers):
    password.append(str(random.randint(0,9)))

for i in range(count_of_symbols):
    password.append(chr(random.choice(symbols)))

p=""

random.shuffle(password)

for char in password:
    p+=char

print(p)