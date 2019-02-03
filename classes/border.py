import turtle

class Border(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.pensize(3)
    
    def draw_border(self):
        self.penup()
        self.setposition(-300,-300)
        self.pendown()
        for _side in range(4):
            self.fd(600)
            self.lt(90)
