import pygame

class Player():
    def __init__(self, playerx, playery):
        self.playerx = playerx
        self.playery = playery

    def renderPlayer(self, gameScreen):
        pygame.draw.rect(gameScreen, (255, 255, 255), (self.playerx, self.playery, 20, 100))
    
    def move(self, ychange):
        if ychange + self.playery > 700:
            return
        if ychange + self.playery < 0:
            return
        self.playery = self.playery + ychange


