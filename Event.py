import turtle as t

def move_forward():

    tom.forward(20)

def move_backward():

    tom.backward(20)

def left():

    new_heading=tom.heading()+20

    tom.setheading(new_heading)

    tom.forward(20)

def right():

    new_heading=tom.heading()-20

    tom.setheading(new_heading)

    tom.forward(20)

def clear_screen():

    tom.clear()

    tom.penup()

    tom.home()

    tom.down()

tom=t.Turtle()

screen=t.Screen()

screen.listen()

screen.onkey(fun=move_forward,key="f")

screen.onkey(fun=move_backward,key="b")

screen.onkey(fun=left,key="l")

screen.onkey(fun=right,key="r")

screen.onkey(fun=clear_screen,key="c")

screen.mainloop()