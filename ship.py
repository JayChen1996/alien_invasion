import pygame


class Ship():
    def __init__(self,ai_settings,screen):
        # screen是一个Surface对象
        self.screen = screen
        self.ai_settings = ai_settings
        # image是一个Surface对象
        self.image = pygame.image.load('images/ship.bmp')
        # rect是一个Rect对象
        self.rect = self.image.get_rect()
        # screen_rect是一个Rect对象
        self.screen_rect = screen.get_rect()
        # centerx是Rect的父类的属性
        self.rect.centerx = self.screen_rect.centerx
        # bottom是Rect的父类的属性
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        self.center = float(self.rect.centerx)


    def blitme(self):
        """blit是Surface的一个函数,在另一个对象上画一幅图"""
        self.screen.blit(self.image,self.rect)

    
    def update(self):
        if self.moving_right and self.center < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.center > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center
        
