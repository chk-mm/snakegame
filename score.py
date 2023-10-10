from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.write("Score: 0", align="center", font=("Courier", 24, "normal"))
        self.score = 0

    def write_score(self,point):
        if point > 0:
            self.score += 10
            self.clear()
            self.write("Score: {}".format(self.score), align="center", font=("Courier", 24, "normal"))
        else:
            self.clear()
            self.write("GAME OVER!!", align="center", font=("Courier", 24, "normal"))

