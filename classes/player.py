import turtle
import platform
import os

class Bullet(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("yellow")
        self.shape("triangle")
        self.penup()
        self.speed(0)
        self.setheading(90)
        self.shapesize(.5,.5)
        self.hideturtle()
        self.bulletspeed = 20
        self.bulletstate = "ready"
      
    # def change_bulletstate(self):
    #   if self.bulletstate == "ready":
    #       self.bulletstate = "fire"
    #   else:
    #       self.bulletstate = "ready" 
    
    def reset(self):
        self.hideturtle()
        self.bulletstate = "ready"
        # Change bullet position so it cannot collide while hidden
        self.setposition(0, -400) 

    def move(self):
        # Move the bullet
        if self.bulletstate == "fire":
            y = self.ycor() + self.bulletspeed
            self.sety(y)

    def boundary_check(self):
        # Check bullet position and change state if it reached top
        if self.ycor() > 275:
            self.hideturtle()
            self.bulletstate = "ready" 

class Player(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        turtle.register_shape("player.gif")
        self.shape("player.gif")
        self.penup()
        self.speed(0)
        self.setposition(0, -250)
        self.setheading(90)
        self.playerspeed = 15
        self.bullet = Bullet()
    
    def play_sound(self, sound_file):
        # Windows
        if platform.system() == 'Windows':
            import winsound
            winsound.PlaySound(sound_file, winsound.SND_ASYNC)
        # Linux
        elif platform.system() == "Linux":
            os.system(f"aplay -q {sound_file}&")
        # Mac
        else:
            os.system(f"afplay {sound_file}&")

    def move_left(self):
        x = self.xcor() - self.playerspeed
        # Keep player from moving outside border
        if x < -280:
            x = -280
        self.setx(x)

    def move_right(self):
        x = self.xcor() + self.playerspeed
        # Keep player from moving outside border
        if x > 280:
            x = 280
        self.setx(x)
    
    def fire_bullet(self):
        if self.bullet.bulletstate == "ready":
            # Play laser sound
            self.play_sound("laser.wav")
            self.bullet.bulletstate = "fire"
            # Move bullet to just above the player
            self.bullet.setposition(self.xcor(), self.ycor() + 10)
            self.bullet.showturtle()