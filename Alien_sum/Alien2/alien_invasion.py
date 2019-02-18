import sys 
import pygame
from setting import Setting
from ship import Ship
import game_functions as gf


def run_game():
    pygame.init()
    ai_setting=Setting()
    screen = pygame.display.set_mode(
        (ai_setting.screen_width,ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship=Ship(screen)

    while True:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_RIGHT:
                    ship.rect.centrex+=1



        screen.fill(ai_setting.bg_color)
        ship.blitme()
    
        pygame.display.flip()

    
    



        







run_game()
