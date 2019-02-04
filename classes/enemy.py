import turtle
import random

class Enemy(turtle.Turtle):

    # All enemies go at the same speed
    enemyspeed = 2
    
    def __init__(self):
        turtle.Turtle.__init__(self)
        turtle.register_shape("invader.gif")
        self.color("green")
        self.shape("invader.gif")
        self.penup()
        self.speed(0)
        self.reset_position()
    
    def reset_position(self):
        x = random.randint(-200,200)
        y = random.randint(100, 250)
        self.setposition(x, y)