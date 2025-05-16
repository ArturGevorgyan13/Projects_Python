import turtle as t

t.color("red","yellow")

t.speed(10)

t.begin_fill()

while True:

    t.forward(300)

    t.left(170)

    if t.heading()==0:

        break

t.end_fill()

t.mainloop()