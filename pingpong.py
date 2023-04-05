# Importing the pygame library 
import pygame
from Paddle import Paddle
from Ball import Ball
 
pygame.init()
 
# Defining the colors
BLACK = (0,0,0)
WHITE = (255,255,255)
 
# Opening in a new window, size
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ping Pong")
 
paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200
 
paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200
 
ball = Ball(WHITE ,10 , 10)
ball.rect.x = 345
ball.rect.y = 195
 
#This will be a list that will contain all the sprites
all_sprites_list = pygame.sprite.Group()
 
# Adding the 2 paddles and the ball to the list of objects
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)
 
# The loop will carry on until the user exits the game
carryOn = True
 
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#Initialise the player scores
scoreA = 0
scoreB = 0
 
#Loop Main Program
while carryOn:
    #Event loop
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: # If the user clicked close
              carryOn = False # sign that we are done so we exit this loop
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_o: #Pressing the o Key will quit the game
                     carryOn=False
 
    #Moving the paddles when the use uses the arrow keys 
    #Player A or "W/S" keys Player B
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)    
 
    #Game logic
    all_sprites_list.update()
    
    #Checking if the ball bounces against any of the 4 walls
    if ball.rect.x>=690:
        scoreA+=1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        scoreB+=1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1]     
 
    #Detect collisions between the ball and the paddles
    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
      ball.bounce()
    
    # First, clearing the screen to black. 
    screen.fill(BLACK)
    #Drawing the net
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
    
    #Now let's draw all the sprites in one go.
    all_sprites_list.draw(screen) 

    #Display scores on the players
    font = pygame.font.Font(None, 50) #size of the numbers
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (250,10))       #middle of the screen
    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (420,10))        # score in each side

    # Updating the screen with what we've drawn.
    pygame.display.flip()
     
    # The limit is 60 frames per second
    clock.tick(50)
 
#Once we exit the main program we can stop the game.
pygame.quit()