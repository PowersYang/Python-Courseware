import random
import pygame

class GameSprite(pygame.sprite.Sprite):
    def __init__(self,image_name,speed=1):
        #调用父类的方法
        super().__init__()

        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed
    def update(self, *args):
        self.rect.y += self.speed

class Background(GameSprite):
    def __init__(self,is_alt = False):
        super().__init__('../images/background.png')
        if is_alt:
            self.rect.y = -700

    def update(self, *args):
        super().update()
        if self.rect.y == 700:
            self.rect.y = -self.rect.y

class Enemy(GameSprite):
    def __init__(self):
        super().__init__('../images/enemy1.png',random.randint(1,3))
        self.rect.x = random.randint(0,423)
        self.rect.bottom = 0
    def update(self, *args):
        super().update()

        if self.rect.y >= 700:
            self.kill()


class Hero(GameSprite):
    flag = 0
    die = False
    def __init__(self):
        super().__init__('../images/me1.png',0)
        self.rect.bottom = 600
        self.rect.centerx  = 240
        self.bullets = pygame.sprite.Group()
        self.time1 = self.time2 = 0
        self.i = 1
        self.speed = 2

    def fire(self):
        bullet = Bullets(self.rect)
        self.bullets.add(bullet)

    def update(self ):

        if Hero.die == True:
            self.speed = 0
            self.time2 = pygame.time.get_ticks()
            Hero.flag = -1
            print('%d %d %d' %(self.time2,self.time1,self.i))
            if self.i == 1:
                print('飞机阵亡')
                self.image = pygame.image.load('../images/me_destroy_1.png')
                self.time1 = self.time2
                self.i += 1
            if self.time2 - self.time1 > 200 and self.i == 2:
                self.image = pygame.image.load('../images/me_destroy_2.png')
                self.i += 1
            if self.time2 - self.time1 > 400 and self.i == 3:
                self.image = pygame.image.load('../images/me_destroy_3.png')
                self.i += 1
            if self.time2 - self.time1 > 600 and self.i == 4:
                self.image = pygame.image.load('../images/me_destroy_4.png')
                self.kill()



        if Hero.flag == 0:
            self.image = pygame.image.load('../images/me2.png')
            Hero.flag = 1
        elif Hero.flag == 1:
            self.image = pygame.image.load('../images/me1.png')
            Hero.flag = 0

    def move(self,direct):
        if direct == 'up':
            if self.rect.top > 0:
                self.rect.y -= self.speed
        elif direct == 'down':
            if self.rect.bottom < 700:
                self.rect.y += self.speed
        elif direct == 'left':
            if self.rect.left > 0:
                self.rect.x -= self.speed
        elif direct == 'right':
            if self.rect.right < 480:
                self.rect.x += self.speed

    # def die(self):
    #     if Hero.die == True:
    #         return
    #     Hero.die = True
    #     self.update()

    def __del__(self):
        print('游戏结束')





class Bullets(GameSprite):
    def __init__(self,hero_rect):
        super().__init__('../images/bullet1.png',-3)
        self.rect.bottom = hero_rect.top
        self.rect.x = hero_rect.centerx

    def update(self, *args):
        super().update()
        if self.rect.y < 0:
            self.kill()

