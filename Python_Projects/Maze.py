#Dependencies

import pygame
from pygame import *
import random


mazemap2=[
0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,
0 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,
1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,
1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,
1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,
1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,
1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,
1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,
1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,
1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,
1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,
1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,
1 ,1 ,1 ,0 ,0 ,0 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,
1 ,1 ,1 ,0 ,1 ,0 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,
1 ,0 ,0 ,0 ,1 ,0 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,
1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,
1 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,
1 ,1 ,1 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,
1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,0 ,
1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,
    
]

#Processing unit
def run():
    running=True
    while running==True:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit() 
                running=False

        
        touchblock=pygame.sprite.spritecollide(player,barriers,None,None)
        clock.tick(60)
        
        sprites.update(2,2,2,2)
        if len(touchblock)!=0 :
            for i in touchblock:
                #if pygame.sprite.collide_rect(player,i):
                    #sprites.update(-3,-3)
                if player.rect.right >= i.rect.left: 
                    sprites.update(-3.1,0,0,0)
                if player.rect.left <= i.rect.right:
                    sprites.update(0,-3.1,0,0)
                if player.rect.bottom >= i.rect.top:
                    sprites.update(0,0,-3.1,0)
                if player.rect.top <= i.rect.bottom:
                    sprites.update(0,0,0,-3.1)        
        
        screen.fill((255,255,255))
        barriers.draw(screen)
        sprites.draw(screen)
        
        
        touch=pygame.sprite.spritecollide(player,finish,False,None)
        
        
        if touch:
            running=False
        
        
        
        
        

        pygame.display.update()

#Display Initials
width=600
height=600
screen=pygame.display.set_mode((width,height))
screen.fill((255,255,255))

clock=pygame.time.Clock()

#Player
class Sprite1(pygame.sprite.Sprite):
    def __init__(self,s_x,s_y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((20,20))
        self.image.fill((150,0,150))
        self.rect=self.image.get_rect()
        self.rect.centerx=s_x
        self.rect.centery=s_y
        self.right=False
        self.left=False
        self.top=False
        self.bottom=False
    
    #Controls
    def update(self,speedx1,speedx2,speedy1,speedy2):
        keystate=pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.rect.x += -speedx1
        if keystate[pygame.K_RIGHT]:
            self.rect.x += speedx2 
        if keystate[pygame.K_UP]:
            self.rect.y += -speedy2
        if keystate[pygame.K_DOWN]:
            self.rect.y += speedy1
        
        
        #OutOfBounds Conditioning
        if self.rect.right>width:
            self.rect.right=width

        if self.rect.left<0:
            self.rect.left=0

        if self.rect.bottom>height:
            self.rect.bottom=height

        if self.rect.top<0:
            self.rect.top=0


#Start Class
class spawnblock1(pygame.sprite.Sprite):
    
    def __init__(self,b_x,b_y,colour):
        self.x=b_x
        self.y=b_y
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((30,30))
        self.image.fill(colour)
        self.rect=self.image.get_rect()
        self.rect.x=self.x
        self.rect.y=self.y
    
    #Spawner For Player
    def give(self): 
        return self.rect.centerx,self.rect.centery


#Barrier Class
class barrier1(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((30,30))
        self.image.fill((0,0,0))
        self.rect=self.image.get_rect()
        self.rect.x=self.x
        self.rect.y=self.y

#all Groups

user=pygame.sprite.Group()
sprites=pygame.sprite.Group()
finish=pygame.sprite.Group()
barriers=pygame.sprite.Group()


sbx,sby=0,0
spawnblock=spawnblock1(sbx,sby,(255,0,0))
spx,spy=spawnblock.give()


player=Sprite1(spx,spy)


ebx,eby=570,570
endblock=spawnblock1(ebx,eby,(0,255,0))

M=20
N=20
bx = 0
by = 0
for i in range(0,M*N):
    if mazemap2[ bx + (by*M) ] == 1:
        barrier=spawnblock1( bx * 30 , by * 30,(0,0,0))
        barriers.add(barrier)
      
    bx = bx + 1
    if bx > M-1:
        bx = 0 
        by = by + 1
    
#addition
finish.add(endblock)
sprites.add(spawnblock,endblock,player)
user.add(player)

        
#run()
run()

