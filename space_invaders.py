# Space Invaders 
# Created using tutorial found at: https://www.youtube.com/watch?v=crV6T3piwHQ

import turtle
import os
import math
import random
import platform

# Set up screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Space Invaders")
screen.bgpic("space_invaders_background.gif")

# Register player and enemy shapes
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")

# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# Set the score to 0
score = 0

# Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = f"Score: {score}"
score_pen.write(scorestring, False, align="left", font=('Arial', 14, 'normal'))
score_pen.hideturtle()

# Create player Turtle object
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

# Create the invaders/enemy
# Choose number of enemies
number_of_enemies = 5
# Create empty list of enemies
enemies = []

# Add enemies to the list
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

# Set enemy features
for enemy in enemies:
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200,200)
    y = random.randint(100, 250)
    enemy.setposition(x,y)

enemyspeed = 2

# Create a player's defense (bullets)
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(.5,.5)
bullet.hideturtle()

bulletspeed = 20

# Define bullet states
# ready = ready to fire
# fire = bullet is firing
bulletstate = "ready"

# Move the player left and right - including boundary-checking
def move_left():
    x = player.xcor() - playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor() + playerspeed
    if x > 280:
      x = 280
    player.setx(x)

def fire_bullet():
    # Bulletstate global if it needs changed
    global bulletstate
    if bulletstate == "ready":
        # Play laser sound
        play_sound("laser.wav")
        bulletstate = "fire"
        # Move bullet to just above the player
        bullet.setposition(player.xcor(), player.ycor() + 10)
        bullet.showturtle()
      
def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + (math.pow(t1.ycor() - t2.ycor(),2)))
    return True if distance < 15 else False

def play_sound(sound_file):
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


# Create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

# MAIN - Game loop
while True:
  # Move enemies
    for enemy in enemies:
        x = enemy.xcor() + enemyspeed
        enemy.setx(x)

        # Move enemy back and forth and down towards player
        if enemy.xcor() > 280 or enemy.xcor() < -280:
            # Move ALL enemies
            for e in enemies:
                y = e.ycor() - 40
                e.sety(y)
            # Change enemy directions
            enemyspeed *= -1
           
      # Check for collision between bullet and enemy
        if isCollision(bullet, enemy):
            # Play explosion sound
            play_sound("explosion.wav")
            # Reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            # Change bullet position so it cannot collide while hidden
            bullet.setposition(0, -400) 
            # Reset enemy position
            x = random.randint(-200,200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            # Update score
            score += 10
            score_pen.clear()
            scorestring = f"Score: {score}"
            score_pen.write(scorestring, False, align="left", font=('Arial'))

        # Check for collison between enemy and player
        if isCollision(player, enemy):
            play_sound("explosion.wav")
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over!")  
            break
  
    # Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor() + bulletspeed
        bullet.sety(y)

    # Check bullet position and change state if it reached top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"
  


  



delay = input("Press any ley to exit...")
