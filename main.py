#Beginning Turn Based Combat Game
#      cd ~/workspace/github.com/Bralimus/turn_combat_game
#   https://pygame-menu.readthedocs.io/en/latest/
import pygame
from menus import GameMenus
from constants import *
from displayable import Displayable, Rectangle, Text

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    drawable = pygame.sprite.Group()

    Displayable.containers = (drawable)
    
    menus = GameMenus()
    txt = Text(500, 500, 200, 400, 
               "Testing a long sentence and super long word pneumonoultramicroscopicsilicovolcanoconiosis", 
               120, visible = True)

    print("Starting Game")

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menus.toggle_pause()
        
        if menus.is_playing:
            screen.fill("cyan")
            for sprite in drawable:
                if sprite.visible:
                    screen.blit(sprite.image, sprite.rect)

        if menus.current_menu.is_enabled():
            menus.current_menu.draw(screen)
            menus.current_menu.update(events)

        pygame.display.update()

    



if __name__ == "__main__":
    main()