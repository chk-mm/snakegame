from turtle import Turtle

positions = [(0, 0), (20, 0), (40, 0)]


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
        for i in range(0,len(self.segments)-1):
            self.segments[i].setheading(90)
            # self.segments[i].forward(20)
            self.move()
