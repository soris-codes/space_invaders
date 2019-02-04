import turtle
class Score(turtle.Turtle):

    def __init__(self):
      turtle.Turtle.__init__(self)
      self.speed(0)
      self.color("white")
      self.penup()
      self.setposition(-290, 280)
      self.score = 0

    def draw_score(self):  
        self.write(f"Score: {self.score}", False, align="left", font=('Arial', 14, 'normal'))
        self.hideturtle()    

    def update_score(self):
        self.score += 10
        self.clear()
        self.draw_score()