import pygame
from pygame.locals import *
from pygame import draw,sprite,surface,image,display,event,time,key

sy=566
sx=1080




class Game:
    width=0
    width1=0
    def __init__(self):
        pygame.init()
        self.running=True
        self.bgout=image.load(r"C:\Users\SHIVINDER\Desktop\Workspace\Mine\Code\vscode\Python\Pygame\images\bg-out.png")
        self.bgmid=image.load(r"C:\Users\SHIVINDER\Desktop\Workspace\Mine\Code\vscode\Python\Pygame\images\bg-mid.png")
        self.floor=image.load(r"C:\Users\SHIVINDER\Desktop\Workspace\Mine\Code\vscode\Python\Pygame\images\floor.png")
        self.car=image.load(r"C:\Users\SHIVINDER\Desktop\Workspace\Mine\Code\vscode\Python\Pygame\images\Car.png")
        self.screensize=self.bgout.get_size()
        self.screen=display.set_mode((self.screensize))
        self.sx=(self.screen.get_rect().centerx)*2
        self.sy=(self.screen.get_rect().centery)*2
    def run(self):
        width=0
        width1=0
        while self.running==True:
            self.screen.blit(self.bgout,(0,0))
            self.screen.blit(self.bgmid,(width,0))
            self.screen.blit(self.bgmid,(width+self.sx,0))
            self.screen.blit(self.bgmid,(width-self.sx,0)) 
            self.screen.blit(self.floor,(width1,0)) 
            self.screen.blit(self.floor,(width1+self.sx,0))
            self.screen.blit(self.floor,(width1-self.sx,0))
            self.screen.blit(self.car,(0,0))
            
            display.update()
            time.Clock().tick(20000)

            press=key.get_pressed()
            if press[K_RIGHT]==True:
                width-=2
                width1-=8
                if width==-self.sx:
                    width=0
                if width1==-self.sx:
                    width1=0
            if press[K_LEFT]==True:
                width+=2
                width1+=8
                if width==self.sx:
                    width=0
                if width1==self.sx:
                    width1=0

            for i in event.get():
                if i.type==QUIT:
                    self.running=False
                    quit()

                
