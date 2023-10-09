from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor('black')
screen.setup(width=600,height=600)
segments = []
positions = [(0,0),(0,20),(0,40)]
for pos in positions:
    new_turtle = Turtle()
    new_turtle.shape('square')
    new_turtle.color('white')
    new_turtle.goto(pos)
    segments.append(new_turtle)


screen.exitonclick()


