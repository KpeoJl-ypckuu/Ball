import pygame
import random
import enemy
import player
import settings
import pygame.freetype
pygame.init()


class Game():
    def __init__(self):
        self.start1 = 1
        self.start_game = 1
        self.window = pygame.display.set_mode(settings.SIZE)
        self.pm = pygame.time.Clock()
        self.player_ball = player.Player_ball()
        self.text_win_and_game_over = ''
        
        self.enemies = []
        self.spawn_enemy = pygame.USEREVENT
        pygame.time.set_timer(self.spawn_enemy,500)


    def draw(self):
        if self.start_game == 1:
            self.window.fill([255,255,255])
            self.player_ball.paint(self.window)
            for paint_enemy in self.enemies:
                paint_enemy.paint(self.window)
            
        
        elif self.start_game == 2:
            self.window.fill([25,25,25])
            for paint_enemy in self.enemies:
                paint_enemy.paint(self.window)
            self.spawn_text_pic = pygame.freetype.Font('шрифт.ttf',50)
            pic_rect = self.spawn_text_pic.render(self.text_win_and_game_over + 'Нажмите R для перезапуска',[255,255,255])
            self.text_pic = pic_rect[0]
            self.text_rect = pic_rect[1]
            self.text_rect.center = [755,540]
            self.window.blit(self.text_pic, self.text_rect)
        
        pygame.display.update()

    
    def event(self):
        events = pygame.event.get()
        for save in events:
            if save.type == pygame.QUIT:
                self.start1 = 3
            
            elif save.type == self.spawn_enemy:
                enemy_balls = enemy.Enemy_ball(self.player_ball)
                self.enemies.append(enemy_balls)
            elif save.type == pygame.KEYDOWN:
                if save.key == pygame.K_r and self.start_game == 2:
                    self.player_ball.ball_player = pygame.rect.Rect([500,500],[100,100])
                    self.enemies = []
                    self.start_game = 1
        

    
    def logic(self):
        self.player_ball.controller()
        for controller_enemy in self.enemies:
            controller_enemy.controller()
        if self.start_game == 1:
            for save in self.enemies:

                if save.rect.colliderect(self.player_ball.ball_player):
                    if self.player_ball.ball_player.width > save.rect.width:
                        self.player_ball.ball_player.width = self.player_ball.ball_player.width + 10
                        self.player_ball.ball_player.height = self.player_ball.ball_player.height + 10
                        self.enemies.remove(save)
                    else:
                        self.start_game = 2
                        self.text_win_and_game_over = 'Вы проиграли ! '
        if self.player_ball.ball_player.width >= 1150:
            self.text_win_and_game_over = 'Вы победили ! '
            self.start_game = 2
                    
                    
        


    def start(self):
        while self.start1 == 1:
            self.draw()
            self.logic()
            self.event()
            self.pm.tick(100)

game = Game()
game.start()

        























