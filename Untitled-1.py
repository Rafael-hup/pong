
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

racket1=Player('ракетка.png', 50, 90, 4, 30, 200)
racket2=Player('ракетка.png', 600, 90, 4, 30, 200)
ball=GameSprite('ball (2).png', 300, 200, 3, 60,40)

font.init()
font1=font.SysFont('Arial', 50)
lose_1=font1.render('player 1 lose', True, (225,215,0))
lose_2=font1.render('player 2 lose', True, (225,215,0))

win_heigth = 500
speed_x=3
speed_y=3
finish=False
game=True
while game:
    if finish != True:
        window.blit(background, (0,0))
        ball.recet()
        racket2.recet()
        racket1.recet()
        racket1.update_l()
        racket2.update_r()
        
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > win_heigth-50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(ball, racket1):
            speed_x *= -1
        if sprite.collide_rect(ball, racket2):
            speed_x *= -1
        
        if ball.rect.x < -20:
            window.blit(lose_1, (200,200))
            finish=True
        if ball.rect.x > 730:
            window.blit(lose_2, (200,200))
            finish=True
    
    else:
        finish=False
        speed_x=3
        speed_y=3
        win_heigth=500
        ball=GameSprite('ball (2).png', 300, 200, 3, 60,40)
        time.delay(3000)

    for e in event.get():
        if e.type == QUIT:
            game=False
       
    clock.tick(FPS)
    display.update() 
