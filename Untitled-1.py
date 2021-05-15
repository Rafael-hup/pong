
from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed, size_x,size_y):
        super(). __init__()
        self.image=transform.scale(image.load(player_image),(size_x,size_y))
        self.speed=player_speed
        self.rect=self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def recet(self):
        window.blit(self.image,(self.rect.x,self.rect.y))


class Player(GameSprite):
    def update_r(self):
        key_pressed=key.get_pressed()

        if key_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < 290:
            self.rect.y += self.speed
    def update_l(self):

        key_pressed=key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < 290:
            self.rect.y += self.speed
        
           
window=display.set_mode((700,500))
background=transform.scale(image.load('background.jpg'), (700,500))
FPS=60
clock=time.Clock()

racket1=Player('ракетка.png', 50, 90, 3, 200, 250)
racket2=Player('ракетка.png', 600, 90, 3, 200, 250)
ball=GameSprite('ball (2).png', 300, 200, 3, 60,40)

game=True
while game:
    window.blit(background, (0,0))
    ball.recet()
    racket2.recet()
    racket1.recet()
    racket1.update_l()
    racket2.update_r()
    for e in event.get():
        if e.type == QUIT:
            game=False
    display.update()
    clock.tick(FPS)

    