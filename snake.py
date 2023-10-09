import time
from turtle import Screen, Turtle

step = 20

screen = Screen()
screen.bgcolor('black')
screen.setup(width=600,height=600)
segments = []
positions = [(0,0),(20,0),(40,0)]
for pos in positions:
    new_turtle = Turtle()
    new_turtle.shape('square')
    new_turtle.color('white')
    new_turtle.pu()
    new_turtle.goto(pos)
    new_turtle.speed('normal')
    # new_turtle.speed(1)
    segments.append(new_turtle)

game_is_on = True
while game_is_on:
    time.sleep(1)
    for i in segments:
        i.speed(1)
        i.forward(step)
        if abs(i.xcor()) > 200:
            i.setheading(270)
        if abs(i.ycor()) >200 :
            i.setheading(0)
        print(i,i.xcor(),i.ycor())


screen.exitonclick()


