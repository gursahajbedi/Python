import pygame as pg
from pygame import *
import random


running=True
screen=pg.display.set_mode((600,600))
clock=pg.time.Clock()


class Box(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image=pg.Surface((40,40))
        self.image.fill((0,0,0))

        self.rect=self.image.get_rect()
        self.rect.x=0
        self.rect.y=500
        self.speedx=0
    
    def shoot(self):
        self.bullet=EnemyBullets(self.rect.x,self.rect.y)
        group.add(self.bullet)
        bullets.add(self.bullet)

    def update(self):
        self.speedx = 0
        keystate = pg.key.get_pressed()
        
        if keystate[pg.K_LEFT]:
            self.speedx = -15
        if keystate[pg.K_RIGHT]:
            self.speedx = 20
        if keystate[pg.K_SPACE]:
            Box.shoot(self)
        self.rect.x += self.speedx
        if self.rect.right > 600:
            self.rect.right = 600
        if self.rect.left < 0:
            self.rect.left = 0
        




class EnemySS(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image=pg.Surface((30,30))
        self.image.fill((0,255,0))
        self.rect=self.image.get_rect()
        self.rect.x=random.randint(10,300)
        self.rect.y=0
        self.speedy=random.randint(3,8)
    def update(self):
        self.rect.y+=self.speedy
        if self.rect.bottom > 600:
            self.rect.y=0
            self.rect.x=random.randint(40,300)
            self.speedy=random.randint(3,8)

class EnemySS2(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image=pg.Surface((30,30))
        self.image.fill((0,0,255))
        self.rect=self.image.get_rect()
        self.rect.x=random.randint(300,560)
        self.rect.y=0
        self.speedy=random.randint(3,8)
    def update(self):
        self.rect.y+=self.speedy
        if self.rect.bottom > 600:
            self.rect.y=0
            self.rect.x=random.randint(300,590)
            self.speedy=random.randint(3,8)

class EnemyBullets(pg.sprite.Sprite):
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        self.image=pg.Surface((10,10))
        self.image.fill((0,0,0))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.speedy=random.randint(1,6)
    def update(self):
        self.rect.y-=self.speedy

        
#group        
group=pg.sprite.Group()
mob=pg.sprite.Group()
bullets=pg.sprite.Group()

player=Box()
group.add(player)

for i in range(5):
    mob1=EnemySS()
    mob2=EnemySS2()

    group.add(mob1,mob2)
    mob.add(mob1,mob2) 

while running:
    clock.tick(60)

    for i in pg.event.get():
        if i.type == pg.QUIT:
            running=False
            pg.quit()
    
    group.update()
    screen.fill((255,255,255))
    group.draw(screen)
    pg.display.update()
    jaag=pg.sprite.groupcollide(bullets,mob,True,True)
    if jaag:
        running=False
    aag=pg.sprite.spritecollide(player,mob,False)
    if aag:
        running=False
         
    


        

                    