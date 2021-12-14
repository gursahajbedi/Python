import pygame
from pygame.locals import *



class Game:
    white='#ffffff'
    black='#000000'
    
    def __init__(self):
        self.x=200
        self.y=250
        pygame.init()
        self.screen=pygame.display.set_mode((400,500))
        self.screen.fill(self.white)
        self.running=True
        self.clock=pygame.time.Clock()

    def sprite(self):
        pygame.draw.circle(self.screen,self.black,(self.x,self.y),20)
        pygame.display.update()

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running=False
                pygame.quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_w:
                    self.y-=10
                if event.key==pygame.K_a:
                    self.x-=10
                if event.key==pygame.K_s:
                    self.y+=10
                if event.key==pygame.K_d:
                    self.x+=10
    def run(self):
        while self.running:
            self.sprite()
            self.move()
            self.clock.tick(60)
App=Game()
App.run()



                

        
        





