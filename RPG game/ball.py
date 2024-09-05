import pygame
import random

startDirection = random.randint(0, 100)

class Ball():
    def __init__(self, ballx, bally):
        self.speedMultiplier = 3
        self.ballx = ballx
        self.bally = bally
        self.ballSpeed = [random.choice([-1, 1]) * self.speedMultiplier, random.uniform(-1, 1) * self.speedMultiplier]
    
    def renderBall(self, gameScreen):
        pygame.draw.circle(gameScreen, (255, 0, 0), (self.ballx, self.bally), 10)

    def collidepoint(self, player):
        if self.ballx >= player.playerx and self.bally >= player.playery and self.ballx <= player.playerx + 20 and self.bally <= player.playery + 100:
            print("Collision detected")
            return True
        
    def update(self):
        self.ballx += self.ballSpeed[0]
        self.bally += self.ballSpeed[1]




