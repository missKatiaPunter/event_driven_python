import turtle
import random
zoe = turtle.Turtle()
food = turtle.Turtle()
wn = turtle.Screen()
wn.setup(600,600)
zoe.speed(1)
zoe.pu()
zoe.pensize(1)
zoe.color("black")
zoe.shape("square")
food.pu()
food.pensize(1)
food.color("pink")
food.shape("square")
x=random.randint(-280,280)
y=random.randint(-280,280)
def placeFood(x,y):
    food.goto(x,y)
    food.stamp()
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
placeFood(x,y)
while zoe.xcor()<300 and zoe.xcor()>-300 and zoe.ycor()<300 and zoe.ycor()>-300:
    if (zoe.xcor()>=(x-20)) and (zoe.xcor()<=(x+20)) and (zoe.ycor()>=(y-20))and (zoe.ycor()<=(y+20)):
        food.clearstamp(1)
        x=random.randint(-280,280)
        y=random.randint(-280,280)
        placeFood(x,y)
    else:
        zoe.clearstamps(1)
        wn.onkey(up,"Up")
        wn.onkey(left,"Left")
        wn.onkey(right,"Right")
        wn.onkey(down,"Down")
        move()
        wn.listen()
wn.listen()
wn.mainloop()
