import pygame
from pygame.locals import *

class Game:
    #colours
    white='#ffffff'
    black='#000000'
    #init
    def __init__(self):
        #pygame init
        pygame.init()
        #display
        self.screen=pygame.display.set_mode((500,600))
        self.screen.fill(self.white)
        pygame.display.update()
        #positions
        self.mouse_pos=None
        #running
        self.running=True
        self.fpsClock = pygame.time.Clock()

    
    def object(self):
        pygame.draw.line(self.screen,self.black,(250,300),self.mouse_pos)
        pygame.display.update()
    
    def mouse(self):
        self.mouse_pos=pygame.mouse.get_pos()
        pygame.display.update()
    def Run(self):
        while self.running:
            for i in pygame.event.get():
                if i.type==pygame.QUIT:
                    self.running=False
                    pygame.quit()
            self.mouse()
            self.object()
            self.fpsClock.tick(60) 
App=Game()
App.Run()
