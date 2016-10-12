import turtle
zoe = turtle.Turtle()
wn = turtle.Screen()
zoe.speed(4)
zoe.pu()
zoe.pensize(1)
zoe.color("black")
zoe.shape("square")
def move():
    zoe.stamp()
    zoe.fd(10)
def up():
    zoe.setheading(90)#turns the turtle up
def down():
    zoe.setheading(270)
def right():
    zoe.setheading(0)
def left():
    zoe.setheading(180)
while True:
    zoe.clearstamps(1)
    wn.onkey(up,"Up")
    wn.onkey(left,"Left")
    wn.onkey(right,"Right")
    wn.onkey(down,"Down")
    wn.listen()
    move()
wn.listen()
wn.mainloop()
