from turtle import Turtle
STYLE = ("Comic Sans", 20, "normal")

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.score = 0
    with open("data.txt") as high_score_data:
      self.high_score = int(high_score_data.read())
    self.color("white")
    self.hideturtle()
    self.penup()
    self.goto(0, 260)
    self.update_scoreboard()

  def update_scoreboard(self):
    self.clear()
    self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=STYLE)

  def increase_score(self):
    self.score += 1
    self.update_scoreboard()

  def reset(self):
    if self.score > self.high_score:
      self.high_score = self.score
      with open("data.txt", mode="w") as high_score_data:
        high_score_data.write(str(self.score))
    self.score = 0
    self.update_scoreboard()
  