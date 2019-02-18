import sys
import pygame

def check_events(ship):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
  
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ship.rect.centrex+=1
                
def update_screen(ai_settings,screen,ship):
    screen.fill(ai_setting.bg_color)
    ship.blitme()
    
    pygame.display.flip()

    
    
