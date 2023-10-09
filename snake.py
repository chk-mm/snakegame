from turtle import Turtle


positions = [(0,0),(20,0),(40,0)]

class Snake:
    segments = []

    def __int__(self):
        for pos in positions:
            new_turtle = Turtle()
            new_turtle.shape('square')
            new_turtle.color('white')
            new_turtle.pu()
            new_turtle.goto(pos)
            new_turtle.speed('normal')
            # new_turtle.speed(1)
            self.segments.append(new_turtle)

    def move(self):
        for segment in self.segments:
            segment.speed(1)
            segment.forward(20)
