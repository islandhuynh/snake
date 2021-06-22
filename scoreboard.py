from turtle import Turtle
STYLE = ("Comic Sans", 20, "normal")

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.score = 0
    self.high_score = 0
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
    self.score = 0
    self.update_scoreboard()

  # def game_over(self):
  #   self.clear()
  #   self.goto(0, 230)
  #   self.color("red")
  #   self.write(f" Game Over.\nFinal Score: {self.score}  ", align="center", font=STYLE)
  