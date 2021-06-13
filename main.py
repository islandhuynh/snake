from turtle import Turtle, Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game by Island Huynh")
screen.tracer(0)

snake = Snake()
food = Food()

screen.onkey(snake.move_up, "w")
screen.onkey(snake.move_down, "s")
screen.onkey(snake.move_left, "a")
screen.onkey(snake.move_right, "d")
screen.listen()

game_is_on = True
while game_is_on:
  screen.update()
  time.sleep(0.1)
  snake.move()

screen.exitonclick()