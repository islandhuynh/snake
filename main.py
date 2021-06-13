from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game by Island Huynh")

snake = Turtle("square")
snake.color("green")
snake.speed(1)

food = Turtle("square")
food.color("red")
food.goto(x=150, y=150)

def move_up():
  snake.setheading(90)

def move_down():
  snake.setheading(270)

def move_left():
  snake.setheading(180)

def move_right():
  snake.setheading(0)

screen.onkey(move_up, "w")
screen.onkey(move_down, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.listen()

while snake.xcor() < 300 and snake.xcor() > -300 and snake.ycor() < 300 and snake.ycor() > -300:
  snake.forward(10)

screen.exitonclick()