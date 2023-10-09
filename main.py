import time
from turtle import Screen,Turtle
from snake import Snake
from fruits import Fruits

screen = Screen()
screen.bgcolor('black')
screen.setup(width=600,height=600)
screen.tracer(0)
screen.listen()

snake = Snake()


screen.addshape('mango.gif')
food = Fruits('mango.gif')

game_is_on = True
while snake.is_dead == 0:
    snake.move()
    screen.onkeypress(fun=snake.go_up, key="Up")
    screen.onkeypress(fun=snake.go_down, key="Down")
    screen.onkeypress(fun=snake.go_right, key="Right")
    screen.onkeypress(fun=snake.go_left, key="Left")
    snake.distance_food(food)
    snake.distance_self()
    snake.distance_wall()
    time.sleep(1)
    screen.update()

screen.exitonclick()


