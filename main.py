from scoreboard import Scoreboard
from turtle import Screen
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
score = Scoreboard()

screen.onkey(snake.move_up, "w")
screen.onkey(snake.move_down, "s")
screen.onkey(snake.move_left, "a")
screen.onkey(snake.move_right, "d")
screen.listen()

game_is_on = True

while game_is_on:
  if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
    score.reset()
    snake.reset()
  screen.update()
  time.sleep(0.1)
  snake.move()
  if snake.head.distance(food) < 20:
    food.refresh()
    snake.extend()
    score.increase_score()
  for seg in snake.segments[1:]:
    if snake.head.distance(seg) < 10:
      score.reset()
      snake.reset()

screen.exitonclick()