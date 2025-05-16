import turtle as t

import random as r

t.colormode(255)

t.speed(10)

while True:

    f=r.randrange(0,255)

    g=r.randrange(0,255)

    b=r.randrange(0,255)

    t.color(f,g,b)

    t.circle(100)

    t.left(5)

    if t.heading()==0:

        break

t.mainloop()