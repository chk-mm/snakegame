import random
import time
from turtle import Screen,Turtle
from snake import Snake
from Food import Food
from score import Score
import os

path = "img"
dir_list = os.listdir(path)



screen = Screen()
screen.bgcolor('black')
screen.setup(width=600,height=600)
screen.tracer(0)
screen.listen()

snake = Snake()


score = Score()

listofdirectory = []
for img in dir_list:
    screen.addshape('img/'+img)
    listofdirectory.append('img/'+img)


food_choice = random.choice(listofdirectory)
food = Food(food_choice)
food.food_pos()



game_is_on = True
while snake.is_dead == 0:
    snake.move()
    screen.onkeypress(fun=snake.go_up, key="Up")
    screen.onkeypress(fun=snake.go_down, key="Down")
    screen.onkeypress(fun=snake.go_right, key="Right")
    screen.onkeypress(fun=snake.go_left, key="Left")
    snake.distance_food(food,score)
    snake.distance_self(score)
    snake.distance_wall(score)
    time.sleep(1)
    screen.update()

screen.exitonclick()


