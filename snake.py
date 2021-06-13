import random
from turtle import Turtle, Screen

class Snake:
  def __init__(self):
    self.segments = []
    self.score = 0
    self.new_snake()
    self.new_food()

  def new_snake(self):
    starting_positions = [(0, 0), (-20, 0), (-40, 0)]
    for position in starting_positions:
      new_segment = Turtle("square")
      new_segment.color("green")
      new_segment.goto(position)
      new_segment.speed(0)
      self.segments.append(new_segment)

  def move(self):
    for seg_num in range(len(self.segments)-1, 0, -1):
      new_x = self.segments[seg_num - 1].xcor()
      new_y = self.segments[seg_num - 1].ycor()
      self.segments[seg_num].goto(new_x, new_y)
    self.segments[0].forward(20)

  def new_food(self):
    food = Turtle("square")
    food.color("red")
    x_position = random.randint(-290, 290)
    y_position = random.randint(-290, 290)
    food.goto(x_position, y_position)