import random
from turtle import Turtle
import fruits

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
        self.is_dead = 0
        self.score = 0
        self.score_display = Turtle()
        self.score_display.speed(0)
        self.score_display.color("white")
        self.score_display.penup()
        self.score_display.hideturtle()
        self.score_display.goto(0, 260)
        self.score_display.write("Score: 0", align="center", font=("Courier", 24, "normal"))

    def write_score(self,point):
        if point > 0:
            self.score += 10
            self.score_display.clear()
            self.score_display.write("Score: {}".format(self.score), align="center", font=("Courier", 24, "normal"))
        else:
            self.score_display.clear()
            self.score_display.write("GAME OVER!!", align="center", font=("Courier", 24, "normal"))

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

    def distance_food(self,food: fruits):
        if self.head.distance(food.fruit_pos) < 20:
            new_turtle = Turtle()
            new_turtle.shape('square')
            color = random.choice(['red','blue','purple','yellow'])
            new_turtle.color(color)
            new_turtle.pu()
            new_turtle.goto(self.segments[0].pos())
            self.segments.insert(0,new_turtle)
            self.head = self.segments[-1]
            food.re_position()
            self.write_score(10)

    def distance_self(self):
        for segment in self.segments:
            if self.head.pos() == segment.pos() and segment != self.head:
                self.is_dead = 1
                print(self.is_dead)
                self.write_score(-1)

    def distance_wall(self):
        if (self.head.xcor() > 290 or
        self.head.xcor() < -290 or
        self.head.ycor() > 290 or
        self.head.ycor() < -290):
            self.is_dead = 1
            print(self.is_dead)
            self.write_score(-1)

