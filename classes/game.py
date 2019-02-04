from classes.player import Bullet, Player
from classes.border import Border
from classes.enemy import Enemy
from classes.score import Score
import turtle
import math
import time

class Game(turtle.Turtle):

    MAX_ENEMIES = 5  

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.score = Score()
        self.player = Player()
        self.enemies = []
    
    def setup(self):
        # Set up screen
        screen = turtle.Screen()
        screen.bgcolor("black")
        screen.title("Space Invaders")
        # Display splash screen for 5 seconds
        # screen.bgpic("splash.gif")
        # time.sleep(5)
        screen.bgpic("space_invaders_background.gif")
        # Draw border
        border = Border()
        border.draw_border()
        # Create enemies
        self.create_enemies()
        # Draw score
        self.score.draw_score()
    
    def create_enemies(self):
        # Add enemies to the list
        for _i in range(self.MAX_ENEMIES):
            self.enemies.append(Enemy())
    
    def isCollision(self, t1, t2):
        distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + (math.pow(t1.ycor() - t2.ycor(),2)))
        return True if distance < 20 else False
    
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
                  # Play explosion sound
                  self.player.play_sound("explosion.wav")
                  # Reset the bullet
                  self.player.bullet.reset()
                  # Reset enemy position
                  enemy.reset_position()
                  # Update score
                  self.score.update_score()

              # Check for collison between enemy and player
              if self.isCollision(self.player, enemy) or enemy.ycor() < -250:
                  # Play explosion sound
                  self.player.play_sound("explosion.wav")
                  # Game is over
                  self.player.hideturtle()
                  enemy.hideturtle()
                  print("Game Over!")  
                  break

          # Move the bullet till it gets to the top boundary
          self.player.bullet.move()
          self.player.bullet.boundary_check()
