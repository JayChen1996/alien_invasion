import sys
import pygame


def run_game():
    pygame.init()
    screen = pygame.display.set_model((1200,00))
    pygame.display.set_caption("Alien Invasion")

    #开始游戏的主循环
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()

run_game()