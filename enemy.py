import pygame
import random

class Enemy_ball: 
    def __init__(self, player):
        self.size = random.randint(player.ball_player.width - 50 , player.ball_player.width + 100)
        self.side = random.randint(1,4)
        # 1 - левая сторона
        # 2 - правая сторона
        # 3 - верх
        # 4 - низ
        if self.side == 1:
            self.rect = pygame.rect.Rect([0,random.randint(0,1780)],[self.size,self.size])
            self.speedX = random.randint(3, 6)
            self.speedY = random.randint(-3,3)
        if self.side == 2:
            self.rect = pygame.rect.Rect([1560,random.randint(0,1780)],[self.size,self.size])
            self.speedX = random.randint(-6, -3)
            self.speedY = random.randint(-3,3)
        if self.side == 3:
            self.rect = pygame.rect.Rect([random.randint(0,2560), 0],[self.size,self.size])
            self.speedY = random.randint(3,6)
            self.speedX = random.randint(-3,3)
        if self.side == 4:
            self.rect = pygame.rect.Rect([random.randint(0,2560), 1780],[self.size,self.size])
            self.speedY = random.randint(-6,-3)
            self.speedX = random.randint(-3,3)

    
        
    def paint(self,window):
        pygame.draw.ellipse(window,[255,0,0],self.rect)
    def controller(self):
        self.rect.y = self.rect.y + self.speedY
        self.rect.x = self.rect.x + self.speedX 