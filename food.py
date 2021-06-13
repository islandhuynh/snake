from turtle import Turtle
import random

class Food(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("square")
    self.penup()
    self.color("red")
    self.speed("fastest")
    x_position = random.randint(-280, 280)
    y_position = random.randint(-280, 280)
    self.goto(x_position, y_position)