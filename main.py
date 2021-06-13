from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game by Island Huynh")
screen.tracer(0)

snake = Snake()

def move_up():
  snake.segments[0].setheading(90)

def move_down():
  snake.segments[0].setheading(270)

def move_left():
  snake.segments[0].setheading(180)

def move_right():
  snake.segments[0].setheading(0)

screen.onkey(move_up, "w")
screen.onkey(move_down, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.listen()

game_is_on = True
while game_is_on:
  screen.update()
  time.sleep(0.1)
  snake.move()

screen.exitonclick()