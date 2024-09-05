import pygame
import sys
from player import Player
from ball import Ball


pygame.init()

myFont = pygame.font.SysFont("Comic Sans MS", 30)

player1 = Player(20, 400)
player2 = Player(760, 400)
ball = Ball(400, 400)

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800

score = 0
gameScreen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()
fps = 30


while True:
    gameScreen.fill((200, 155, 205))

    textSurface = myFont.render(f"score:{score}", False, (170, 40, 10))
    gameScreen.blit(textSurface, (0,0))
    ball.update()
    player1.renderPlayer(gameScreen)
    player2.renderPlayer(gameScreen)
    ball.renderBall(gameScreen)

    events = pygame.event.get()
    
    keys = pygame.key.get_pressed()
    
    collide = ball.collidepoint(player1)
    collide2 = ball.collidepoint(player2)

    if not 0 <= ball.ballx <= 800:
        sys.exit()

    if collide == True or collide2 == True:
        ball.ballSpeed[0] *= -1
        score += 1
    if not 0 <= ball.bally <= 800:
        ball.ballSpeed[1] *= -1

    if keys[pygame.K_w]:
        player1.move(-5)
        if collide == True:
            ball.ballSpeed[1] += -1 
    if keys[pygame.K_s]:
        player1.move(5)
        if collide == True:
            ball.ballSpeed[1] += 1

    if keys[pygame.K_UP]:
        player2.move(-5)
        if collide2 == True:
            ball.ballSpeed[1] += -1
    if keys[pygame.K_DOWN]:
        player2.move(5)
        if collide2 == True:
            ball.ballSpeed[1] += 1

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()       

    clock.tick(fps)
    pygame.display.update()


# End