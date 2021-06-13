from turtle import Turtle, Screen
import random
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game by Island Huynh")
screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []
# class Snake:
#   def __init__(self):
#     pass

# snake = []
# for x in range(3):
#   snake_block = Turtle("square")
#   snake_block.color("green")
#   snake_block.goto(-20*x, 0)

# food = Turtle("square")
# food.color("red")
# food.goto(x=150, y=150)

# def move_up():
#   snake.setheading(90)

# def move_down():
#   snake.setheading(270)

# def move_left():
#   snake.setheading(180)

# def move_right():
#   snake.setheading(0)

# screen.onkey(move_up, "w")
# screen.onkey(move_down, "s")
# screen.onkey(move_left, "a")
# screen.onkey(move_right, "d")
# screen.listen()

# while snake[0].xcor() < 300 and snake[0].xcor() > -300 and snake[0].ycor() < 300 and snake[0].ycor() > -300:
#   snake.forward(10)

for position in starting_positions:
  new_segment = Turtle("square")
  new_segment.color("green")
  new_segment.goto(position)
  segments.append(new_segment)

def move_up():
  segments[0].setheading(90)

def move_down():
  segments[0].setheading(270)

def move_left():
  segments[0].setheading(180)

def move_right():
  segments[0].setheading(0)

screen.onkey(move_up, "w")
screen.onkey(move_down, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.listen()

game_is_on = True
while game_is_on:
  screen.update()
  time.sleep(0.1)
  for seg_num in range(len(segments)-1, 0, -1):
    new_x = segments[seg_num - 1].xcor()
    new_y = segments[seg_num - 1].ycor()
    segments[seg_num].goto(new_x, new_y)
  segments[0].forward(20)
  if segments[0].xcor() > 300 or segments[0].xcor() < -300 or segments[0].ycor() > 300 or segments[0].ycor() < -300:
    game_is_on = False

screen.exitonclick()