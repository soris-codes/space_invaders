from classes.player import Bullet, Player
from classes.border import Border
from classes.enemy import Enemy
import turtle
import os
import math
import platform

class Game(turtle.Turtle):

    MAX_ENEMIES = 5  

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.score = 0
        self.player = Player()
        self.enemies = []
    
    def setup(self):
        # Set up screen
        screen = turtle.Screen()
        screen.bgcolor("black")
        screen.title("Space Invaders")
        screen.bgpic("space_invaders_background.gif")
        # Draw border
        border = Border()
        border.draw_border()
        # Create enemies
        self.create_enemies()
    
    def create_enemies(self):
        # Add enemies to the list
        for _i in range(self.MAX_ENEMIES):
            self.enemies.append(Enemy())
    
    def isCollision(self, t1, t2):
        distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + (math.pow(t1.ycor() - t2.ycor(),2)))
        if distance < 20:
            # Play explosion sound
            self.play_sound("explosion.wav")
            return True
        else:
            return False

    def update_displayed_score(self):
        self.score += 10
        self.clear()
        self.write(f"Score: {self.score}", False, align="left", font=('Arial', 14, 'normal'))
    
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
    
    def play_game(self):  
      # Set up game screen, border, and enemies
      self.setup()
  
      # Define keyboard bindings
      turtle.listen()
      turtle.onkey(self.player.move_left, "Left")
      turtle.onkey(self.player.move_right, "Right")
      turtle.onkey(self.player.fire_bullet, "space")

      # Game loop 
      while True:
          # Move enemies back and forth toward player
          for enemy in self.enemies:
              x = enemy.xcor() + Enemy.enemyspeed
              enemy.setx(x)

              if enemy.xcor() > 280 or enemy.xcor() < -280:
                  # Move ALL enemies
                  for e in self.enemies:
                      y = e.ycor() - 40
                      e.sety(y)

                  # Change enemy directions
                  Enemy.enemyspeed *= -1

              # Check for collision between bullet and enemy
              if self.isCollision(self.player.bullet, enemy):
                  # Reset the bullet
                  self.player.bullet.reset()
                  # Reset enemy position
                  enemy.reset_position()
                  # Update score
                  self.update_displayed_score()

              # Check for collison between enemy and player
              if self.isCollision(self.player, enemy):
                  # Game is over
                  self.player.hideturtle()
                  enemy.hideturtle()
                  print("Game Over!")  
                  break

          # Move the bullet till it gets to the top boundary
          self.player.bullet.move()
          self.player.bullet.boundary_check()
