# In this example.py you will learn how to make a very simple game using the pygame library.
# One of the best ways of learning to program is by writing games.
# Pygame is a collection of modules in one package.
# You will need to install pygame.
# To do so:
# 1) open the command line interface on your computer,
# 2) cd to the directory that this task is located in,
# 3) follow the instructions here: https://www.pygame.org/wiki/GettingStarted
# 4) if you need help using pip, see here: https://projects.raspberrypi.org/en/projects/using-pip-on-windows

import pygame # Imports a game library that lets you use specific functions in your program.
import random # Import to generate random numbers. 

# Initialize the pygame modules to get everything started.

pygame.init() 

# The screen that will be created needs a width and a height.

screen_width = 1040
screen_height = 680
screen = pygame.display.set_mode((screen_width,screen_height)) # This creates the screen and gives it the width and height specified as a 2 item sequence.

# This creates the player and gives it the image found in this folder (similarly with the enemy image). 

player = pygame.image.load("game/image.png")
enemy = pygame.image.load("game/enemy.png")
monster = pygame.image.load("game/monster.jpg")
monster_two =pygame.image.load("game/monsterTWO.jpg")
prize = pygame.image.load("game/prize.jpg")

# Get the width and height of the images in order to do boundary detection (i.e. make sure the image stays within screen boundaries or know when the image is off the screen).

image_height = player.get_height()
image_width = player.get_width()
enemy_height = enemy.get_height()
enemy_width = enemy.get_width()
monster_height = monster.get_height()
monster_width = monster.get_width()
monster_two_height = monster_two.get_height()
monster_two_width = monster_two.get_width()
prize_height = prize.get_height()
prize_width = prize.get_width()



print("This is the height of the player image: " +str(image_height))
print("This is the width of the player image: " +str(image_width))
print("This is the height of the enemy image: " + str(enemy_height))
print("This is the width of the enemy image: " + str(enemy_width))
print("This is the height of the monster image: " + str(monster_height))
print("This is the width of the monster image: " + str(monster_width))
print("This is the height of the monster 2 image: " + str(monster_two_height))
print("This is the width of the monster 2 image: " + str(monster_two_width))
print("This is the height of the prize image: " + str(prize_height))
print("This is the width of the prize image: " + str(prize_width))



# Store the positions of the player and enemy as variables so that you can change them later. 

playerXPosition = 100
playerYPosition = 50
prizeXPosition = 800 #keep X position of prize fixed
prizeYPosition = random.randint(0,screen_height - prize_height) #randomize the Y position

# Make the enemy start off screen and at a random y position.

enemyXPosition =  screen_width
enemyYPosition = random.randint(0, screen_height - enemy_height)

# Make the second enemy start off screen and at a random y position.

monsterXPosition = screen_width
monsterYPosition = random.randint(0, screen_height - monster_height)

# Make the third enemy start off screen and at a random y position.

monster_two_XPosition = screen_width
monster_two_YPosition = random.randint(0,screen_height - monster_two_height)


#the code below is to ensure that there will always be some distance created between the enemy and monster two
#this is to ensure that they are never too close together otherwise the game gets boring

v = enemyYPosition - monster_two_YPosition #use the Y position as that is the position you want to be different
print(v)


p = False
while (p == False):
    if (v < 100): #if v < 100
        monster_two_YPosition += 100 #add 100px to the Y position of monster Two
        p = True
    elif (v >= 100): #otherwise don't bother and leave as is
        p = True

print("enemyXpos: {} enemyYpos: {} ".format(enemyXPosition,enemyYPosition))
print("monsterXpos: {} monsterYpos: {} ".format(monsterXPosition,monsterYPosition))
print("monster_two_Xpos: {} monster_two_Ypos: {} ".format(monster_two_XPosition,monster_two_YPosition))
# This checks if the up or down key is pressed.
# Right now they are not so make them equal to the boolean value (True or False) of False. 
# Boolean values are True or False values that can be used to test conditions and test states that are binary, i.e. either one way or the other. 

keyUp= False
keyDown = False
keyRight = False
keyLeft = False

# This is the game loop.
# In games you will need to run the game logic over and over again.
# You need to refresh/update the screen window and apply changes to 
# represent real time game play. 

while 1: # This is a looping structure that will loop the indented code until you tell it to stop(in the event where you exit the program by quitting). In Python the int 1 has the boolean value of 'true'. In fact numbers greater than 0 also do. 0 on the other hand has a boolean value of false. You can test this out with the bool(...) function to see what boolean value types have. You will learn more about while loop structers later. 

    screen.fill(0) # Clears the screen.
    screen.blit(player, (playerXPosition, playerYPosition))# This draws the player image to the screen at the postion specfied. I.e. (100, 50).
    # draw images on screen based on X and Y position
    screen.blit(monster, (monsterXPosition,monsterYPosition))
    screen.blit(enemy, (enemyXPosition, enemyYPosition))
    screen.blit(monster_two, (monster_two_XPosition, monster_two_YPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))

    
    pygame.display.flip()# This updates the screen. 
    
    # This loops through events in the game.
    
    for event in pygame.event.get():
    
        # This event checks if the user quits the program, then if so it exits the program. 
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        # This event checks if the user press a key down.
        
        if event.type == pygame.KEYDOWN:
        
            # Test if the key pressed is the one we want.
            
            if event.key == pygame.K_UP: # pygame.K_UP represents a keyboard key constant. 
                keyUp = True
            if event.key == pygame.K_DOWN: # user presses down
                keyDown = True
            if event.key == pygame.K_RIGHT: #user presses right
                keyRight = True
            if event.key == pygame.K_LEFT: #user presses left
                keyLeft = True
        
        # This event checks if the key is up(i.e. not pressed by the user).
        
        if event.type == pygame.KEYUP:
        
            # Test if the key released is the one we want.
            
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_RIGHT:
                keyRight = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            
    # After events are checked for in the for loop above and values are set,
    # check key pressed values and move player accordingly.
    
    # The coordinate system of the game window(screen) is that the top left corner is (0, 0).
    # This means that if you want the player to move down you will have to increase the y position. 
    
    if keyUp == True:
        if playerYPosition > 0 : # This makes sure that the user does not move the player above the window.
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < screen_height - image_height:# This makes sure that the user does not move the player below the window.
            playerYPosition += 1
    if keyLeft == True: # move player left
        if playerXPosition > 0:
            playerXPosition -=1
    if keyRight == True: # move player right
        if playerXPosition < screen_width - image_width:
            playerXPosition += 1
    # Check for collision of the enemy with the player.
    # To do this we need bounding boxes around the images of the player and enemy.
    # We the need to test if these boxes intersect. If they do then there is a collision.
    
    # Bounding box for the player:
    
    playerBox = pygame.Rect(player.get_rect())
    
    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image. 
    
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    # Bounding box for the prize:

    prizeBox = pygame.Rect(prize.get_rect())
    #The following updates the prizeBox position to the prize's position,
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition

    # Bounding box for the enemy:
    enemyBox = pygame.Rect(enemy.get_rect())
    #The following updates the ememyBox position to the ememy's position,
    enemyBox.top = enemyYPosition
    enemyBox.left = enemyXPosition

    # Bounding box for the monster:
    monsterBox = pygame.Rect(monster.get_rect())
    #The following updates the monsterBox position to the monster's position,
    monsterBox.top = monsterYPosition
    monsterBox.left = monsterXPosition

    # Bounding box for the second monster:
    monster_two_Box = pygame.Rect(monster_two.get_rect())
    #The following updates the monster_twoBox position to the monster_two's position,
    monster_two_Box.top = monster_two_YPosition
    monster_two_Box.left = monster_two_XPosition

# if player collides with monster
    if playerBox.colliderect(monsterBox):
        print("you lose!")
        pygame.quit()
        exit(0)

# if player collides with monster two
    if playerBox.colliderect(monster_two_Box):
        print("you lose!")
        pygame.quit()
        exit(0)

    # Test collision of the boxes:
# if player collides with enemy
    if playerBox.colliderect(enemyBox):
    
        # Display losing status to the user: 
        
        print("You lose!")
       
        # Quite game and exit window: 
        
        pygame.quit()
        exit(0)
        
    # If the enemy is off the screen the user wins the game:
# if player collides with prize
    if playerBox.colliderect(prizeBox):
    
        # Display wining status to the user: 
        
        print("You win!")
        
        # Quite game and exit window: 
        pygame.quit()
        
        exit(0)
    
 
    
    # Make enemy approach the player.
    enemyXPosition -= 0.15
    # Make monster approach the player
    monsterXPosition -= 0.5
    # Make prize approach the player
    monster_two_XPosition -= 0.2

    # ================The game loop logic ends here. =============
  
