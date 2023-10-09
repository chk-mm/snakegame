import time
from turtle import Screen,Turtle
from snake import Snake




screen = Screen()
screen.bgcolor('black')
screen.setup(width=600,height=600)
screen.tracer(0)
screen.listen()


s_screenlisten = Turtle()



snake = Snake()

print(len(snake.segments))

game_is_on = True
while game_is_on:
    snake.move()
    screen.onkeypress(fun=snake.go_up, key="Up")
    screen.onkeypress(fun=snake.go_down, key="Down")
    screen.onkeypress(fun=snake.go_right, key="Right")
    screen.onkeypress(fun=snake.go_left, key="Left")
    time.sleep(1)
    screen.update()


screen.exitonclick()


