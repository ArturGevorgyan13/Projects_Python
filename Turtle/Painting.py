import turtle as t

import random 

t.hideturtle()

t.colormode(255)

t.speed(10)

t.up()

for i in range(100):

    r=random.randint(0,255)

    g=random.randint(0,255)

    b=random.randint(0,255)

    x=random.randint(-300,300)

    y=random.randint(-300,300)

    t.goto(x,y)

    t.dot(30,(r,g,b))

t.mainloop()