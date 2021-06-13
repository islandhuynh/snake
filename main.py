from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

snake = Turtle("square")
snake.color("green")

food = Turtle("square")
food.color("red")
food.goto(x=150, y=150)

screen.exitonclick()