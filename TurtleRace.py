import turtle
import random     

colors={

    "red":True,
    "blue":True,
    "green":True,
    "yellow":True,
    "pink":True,
    "brown":True,
    "orange":True,
    "teal":True,
    "tomato":True,
    "tan":True

}

WIDTH,HEIGHT=400,400

def set_color(t):

    c=random.choice(list(colors.keys()))

    while colors[c]==False:

        c=random.choice(list(colors.keys()))

    t.color(c)

    colors[c]=False

def number_of_turtles():

    count=int(input("How many turtles you want to race(2-10)?\n"))
    
    if count>=2 and count<=10:

        return count

    else:

        print("Input is not in given range! Try again!")

        return number_of_turtles()
    
def create_turtles(number):

    turtles=[]

    for i in range(1,number_turtles+1):

        new_turtle=turtle.Turtle()

        new_turtle.up()

        new_turtle.shape("turtle")

        set_color(new_turtle)

        new_turtle.left(90)

        new_turtle.goto(-WIDTH//2+i*X_SPACE,-HEIGHT//2+20)

        turtles.append(new_turtle)

    return turtles

def race():

    race_on=True

    while race_on:

        for t in turtles:

            distance=random.randint(1,20)

            t.forward(distance)

            x,y=t.pos()

            if y>=HEIGHT//2-30:

                print(f"The winner is {t.pencolor()}!")

                race_on=False

                break

number_turtles=number_of_turtles()

X_SPACE=WIDTH//(number_turtles+1)

turtle.setup(WIDTH,HEIGHT)

turtles=create_turtles(number_turtles)

race()

turtle.mainloop()