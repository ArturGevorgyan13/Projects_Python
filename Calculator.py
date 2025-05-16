import os

def clean_screen():
    os.system('clear')

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

print("* * * * * * *Welcome to my CALCULATOR* * * * * * *")

input("Please, enter if you want to start!")

operations={"+":add,
            "-":sub,
            "*":mul,
            "/":div}

def calculator():
    clean_screen()

    num1=float(input("Please, enter the first number: "))

    flag=True

    while flag:
        for operator in operations:
            print(operator)

        operator=input("Choose an operation: ")

        num2=float(input("Please, enter the second number: "))

        function=operations[operator]

        output=function(num1,num2)

        print(f"{num1}{operator}{num2}={output}")

        case=input(f"Enter 'y' to continue calculation with {output},'n' to start a new calculation,'x' to exit: ").lower()

        if case=='y':
            num1=output
        elif case=='n':
            flag=False
            calculator()
        else:
            flag=False
            print("Bye!")

calculator()