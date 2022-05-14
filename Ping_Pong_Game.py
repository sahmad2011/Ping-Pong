from cgitb import text
from pygame import *
from random import randint
 
class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed_x, player_speed_y, img_w, img_h):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (img_w,img_h))
       self.speed_x = player_speed_x
       self.speed_y = player_speed_y
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
 
class Player(GameSprite):
   def update1(self):
       if keys_pressed[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed_y
       if keys_pressed[K_s] and self.rect.y < 455:
           self.rect.y += self.speed_y
   def update2(self):
       if keys_pressed[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed_y
       if keys_pressed[K_DOWN] and self.rect.y < 455:
           self.rect.y += self.speed_y
 
class Enemy(GameSprite):
   def update(self):
        global score1,score2
        if self.rect.y > 465:
            self.speed_y = -1*self.speed_y
        if self.rect.y < -20:
            self.speed_y = -1*self.speed_y
        if self.rect.x > 665:
            self.speed_x = -1*self.speed_x
            score1 += 1
            self.rect.x = 300
            self.rect.y = 200
        if self.rect.x < -20:
            self.speed_x = -1*self.speed_x
            score2 += 1
            self.rect.x=300
            self.rect.y = 200
        
        
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

score1 = 0
score2 = 0
 
 
window = display.set_mode((700, 500))
display.set_caption("Ping Pong")
background = transform.scale(image.load("background.jpg"), (700, 500))
 
 
 
paddle1 = Player("pong_paddle.png",0,400,0,5,30,90)
paddle2 = Player("pong_paddle.png",670,400,0,5,30,90)
ball = Enemy("tennis_ball.png",300,300,5,2,65,65)
 
 
 

#game loop
run = True
finish = False
clock = time.Clock()
FPS = 60
font.init()
font1 = font.Font(None,80)
font2 = font.Font(None,36)
win1 = font1.render("PLAYER 1 WINS!", True,(255, 215, 0))
win2 = font2.render("PLAYER WINS!", True, (255, 0, 0))
while run:
 
    for e in event.get():
        if e.type == QUIT:
           run = False
  
    if finish != True:
        window.blit(background,(0, 0))
        keys_pressed = key.get_pressed()

        text1 = font2.render("Player 1: " + str(score1), 1, (255,255,255))
        window.blit(text1,(10,20))
 
        text2 = font2.render("Player 2: " + str(score2), 1, (255,255,255))
        window.blit(text2,(550,20))

        paddle1.reset()
        paddle2.reset()
        ball.reset()
    
    
        paddle1.update()
        paddle2.update()
        ball.update()
        
        if sprite.collide_rect(paddle1, ball) or sprite.collide_rect(paddle2, ball):
            ball.speed_x *= -1
            ball.speed_y *= -1
        if score1 >= 10:
            finish=True
            window.blit(win1,(200, 200))
        if score1 >= 10:
            finish=True
            window.blit(win2,(200, 200))
    
        display.update()
        clock.tick(FPS)


