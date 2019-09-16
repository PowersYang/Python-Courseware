import time
import pygame
from project.plane_sprites import *
class PlaneGame(object):

    #初始化游戏
    def __init__(self,size,backgroud):
        self.screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()
        background0 = Background()
        background1 = Background(True)
        self.hero = Hero()
        self.game_group = pygame.sprite.Group(background0,background1)
        self.hero_group = pygame.sprite.Group(self.hero)
        self.enemy_group = pygame.sprite.Group()

        self.creat_enemy = pygame.USEREVENT

        pygame.time.set_timer(self.creat_enemy,1000)

        self.time1 = 0
        self.time2 = 0

    #事件监听
    def __even_handler(self):

        for even in pygame.event.get():

            if even.type == pygame.QUIT:
                self.__exit_game()

            if even.type == self.creat_enemy:
                enemy = Enemy()
                self.enemy_group.add(enemy)

            if even.type == pygame.KEYDOWN and even.key == pygame.K_SPACE:
                self.time2 = pygame.time.get_ticks()
                if self.time2 - self.time1 < 250:
                    break
                self.hero.fire()
                self.time1 = self.time2





        keys_passed = pygame.key.get_pressed()
        if keys_passed[pygame.K_UP]:
            self.hero.move('up')
        elif keys_passed[pygame.K_DOWN]:
            self.hero.move('down')
        elif keys_passed[pygame.K_LEFT]:
            self.hero.move('left')
        elif keys_passed[pygame.K_RIGHT]:
            self.hero.move('right')



    #碰撞检测
    def __check_collied(self):
        pygame.sprite.groupcollide(self.enemy_group,self.hero.bullets,True,True)
        go_die = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
        if len(go_die)  > 0:
            Hero.die = True

    #元素更新
    def __update_sprites(self):
        self.game_group.update()
        self.hero_group.update()
        self.enemy_group.update()
        self.hero.bullets.update()
        self.game_group.draw(self.screen)
        self.hero_group.draw(self.screen)
        self.enemy_group.draw(self.screen)
        self.hero.bullets.draw(self.screen)


    #游戏结束
    def __game_over(self):
        self.screen.blit(self.backgroud,(0,0))

    #退出游戏
    @staticmethod
    def __exit_game():
        pygame.quit()
        exit()

    #游戏的主循环
    def start(self,fps):

        while True:
            #设置帧率
            self.clock.tick(fps)
            #事件监听
            self.__even_handler()
            #碰撞检测
            self.__check_collied()
            #更新元素
            self.__update_sprites()
            #更新显示
            pygame.display.update()

if __name__ == '__main__':
    game = PlaneGame((480,700),'../images/background.png')
    game.start(40)
