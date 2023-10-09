from turtle import Turtle

positions = [(0, 0), (20, 0), (40, 0)]
BOTTOM = 270
UP = 90
LEFT = 180
RIGHT = 360

class Snake:
    def __init__(self):
        self.segments = []
        for pos in positions:
            new_turtle = Turtle()
            new_turtle.shape('square')
            new_turtle.color('white')
            new_turtle.pu()
            new_turtle.goto(pos)
            new_turtle.speed('normal')
            self.segments.append(new_turtle)
        self.head = self.segments[-1]

    def move(self):
        for i in range(0,len(self.segments)-1):
            current = self.segments[i]
            next_one = self.segments[i+1]
            current.goto(next_one.pos())
        self.head.forward(20)


    def go_up(self):
        if self.head.heading() != BOTTOM:
            self.head.setheading(UP)

    def go_down(self):
        if self.head.heading() != UP:
            self.head.setheading(BOTTOM)

    def go_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def go_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

