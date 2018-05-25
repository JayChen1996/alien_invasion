
import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from pygame import init
from pygame import display
import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.scree_width,ai_settings.scree_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings,screen)
    """Group() 是Sprite模块中的类"""
    bullets = Group()
    gf.update_screen(ai_settings,screen,ship,bullets)

    #开始游戏的主循环
    while True:
        #监听键盘和鼠标事件
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        print(len(bullets))

        gf.update_screen(ai_settings,screen,ship,bullets)
        



run_game()