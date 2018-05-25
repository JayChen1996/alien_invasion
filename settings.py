class Settings():
    """存储本游戏的所有设置的类"""
    
    def __init__(self):
        #屏幕设置
        self.scree_width = 800
        self.scree_height = 500
        #用RGB元组表示的颜色
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 1

        #子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 30