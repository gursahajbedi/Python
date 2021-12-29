import pygame
from pygame.locals import *
from pygame import display,event,time,draw,surface,image,transform,font
from Game import *


class Homescreen:
    def __init__(self):
        
        self.running=True
        
        #initializing pygame
        pygame.init()
        
        #images
        self.bgout=image.load(r"C:\Users\SHIVINDER\Desktop\Workspace\Mine\Code\vscode\Python\Pygame\images\bg-out.png")
        self.bgmid=image.load(r"C:\Users\SHIVINDER\Desktop\Workspace\Mine\Code\vscode\Python\Pygame\images\bg-mid.png")
        self.floor=image.load(r"C:\Users\SHIVINDER\Desktop\Workspace\Mine\Code\vscode\Python\Pygame\images\floor.png")
        
        #display
        self.screensize=self.bgout.get_size()
        self.screen=display.set_mode((self.screensize))
        self.sx=(self.screen.get_rect().centerx)*2
        self.sy=(self.screen.get_rect().centery)*2
        display.set_caption("MazeGame")
        display.update()
    
    def text(self,textsize=int,text=str,textfont=str):
        fonts=font.SysFont(textfont,textsize)
        return fonts.render(text,True,(255,255,255))
    
    def run(self):
        width=0
        width1=0
        while self.running==True:
            self.screen.blit(self.bgout,(0,0))
            self.screen.blit(self.bgmid,(width,0))
            self.screen.blit(self.bgmid,(width+self.sx,0)) 
            self.screen.blit(self.floor,(width1,0)) 
            self.screen.blit(self.floor,(width1+self.sx,0))
            img=self.text(100,"Astasia","Century Gothic")
            self.screen.blit(img,((self.sx/2)-150,(self.sy/2)-100))
            img2=self.text(30,"Drifting towards the Abyss","Century Gothic")
            self.screen.blit(img2,((self.sx/2)-165,(self.sy/2)))

            img3=self.text(25,"Press Enter To Continue","Century Gothic")
            self.screen.blit(img3,((self.sx/2)-125,(self.sy/2)+130))

            width-=1
            width1-=4
            display.update()
            if width==-self.sx:
                width=0
            if width1==-self.sx:
                width1=0
            
            
            
            time.Clock().tick(300)
            
            
            
            for i in event.get():
                if i.type==QUIT:
                    self.running=False
                    pygame.quit()
                if i.type==KEYDOWN:
                    if i.key == K_RETURN:
                        x=Game()
                        x.run()
                        self.running=False
                        pygame.quit()
                                   
                        
                        
                          


                
        

x=Homescreen()
x.run()

        