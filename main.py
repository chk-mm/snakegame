import time
from turtle import Screen

from snake import Snake


screen = Screen()
screen.bgcolor('black')
screen.setup(width=600,height=600)
screen.tracer(0)

snake = Snake()

game_is_on = True
while game_is_on:
    screen.listen()
    snake.move()
    time.sleep(1)
    screen.update()


screen.exitonclick()


