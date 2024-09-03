import pygame

class Player_ball: 
    def __init__(self):
        self.speed = 5
        self.ball_player = pygame.rect.Rect([500,500],[100,100])
    def paint(self,window):
        pygame.draw.ellipse(window,[0,255,0],self.ball_player)
    def controller(self):
        self.ball_player.center = pygame.mouse.get_pos()
        