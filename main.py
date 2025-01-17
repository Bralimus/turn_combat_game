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
    header_b = Text(SCREEN_WIDTH/2 - 300, 0, 600, 100, "Battle!", 120, visible = True)
    menu_button_b = Text(0, 0, 150, 70, "Menu", 80, colour = None, visible = True)
    help_button_b = Text(SCREEN_WIDTH - 100, 0, 150, 70, "?", 80, colour = None, visible = True)

    player_b = Rectangle(SCREEN_WIDTH/3 - 200, SCREEN_HEIGHT/3 - 50, 400, 400, "blue", True)
    player_hp_border_b = Rectangle(SCREEN_WIDTH/3 - 250, 250, 500, 100, "black", True)
    player_hp_b = Rectangle(SCREEN_WIDTH/3 - 240, 260, 480, 80, "green", True) #change size based on %hp
    player_hp_number_b = Text(SCREEN_WIDTH/3 - 240, 260, 480, 80, 
                              "HP: 100/100", #will change based on damage taken and max hp stat
                              100, colour = None, visible = True)

    enemy_b = Rectangle(SCREEN_WIDTH*2/3 - 200, SCREEN_HEIGHT/3 - 50, 400, 400, "red", True)
    enemy_hp_border_b = Rectangle(SCREEN_WIDTH*2/3 - 250, 250, 500, 100, "black", True)
    enemy_hp_b = Rectangle(SCREEN_WIDTH*2/3 - 240, 260, 480, 80, "green", True) #change size based on %hp
    enemy_hp_number_b = Text(SCREEN_WIDTH*2/3 - 240, 260, 480, 80, 
                         "HP: 100/100", #will change based on damage taken and max hp stat
                         100, colour = None, visible = True)
    
    bottom_bar_b = Rectangle(0, SCREEN_HEIGHT - 400, SCREEN_WIDTH, 400, "black", True)
    attack_info_background_b = Rectangle(SCREEN_WIDTH/3 + 10, SCREEN_HEIGHT - 390, SCREEN_WIDTH/3 - 20, 380, 
                                         "cyan", #will be player colour slightly faded once shift is updated
                                         True)
    attack_info_b = Text(SCREEN_WIDTH/3 + 20, SCREEN_HEIGHT - 300, SCREEN_WIDTH/3 - 40, 200, 
                         "Will display information about the attack, what it does and update based on attack selected", 120,
                          colour = None, visible = True)
    attack_name_b = Text(SCREEN_WIDTH/2 - 115, SCREEN_HEIGHT - 380, 230, 70, "Attack 1", 120, visible = True)
    attack_border_b = Rectangle(SCREEN_WIDTH/2 - 125, SCREEN_HEIGHT - 90, 250, 70, visible = True)
    attack_b = Text(SCREEN_WIDTH/2 - 115, SCREEN_HEIGHT - 80, 230, 60, "Attack", 120, colour = "red", visible = True)
    

    player_attacks_b = Rectangle(10, SCREEN_HEIGHT - 390, SCREEN_WIDTH/3 - 10, 380, "blue", True)
    player_attack_1_b = Text(20, SCREEN_HEIGHT - 380, (SCREEN_WIDTH/3 - 10)/2 - 15, 175, "Attack 1", 120, colour = "white", visible = True)
    player_attack_2_b = Text(15 + ((SCREEN_WIDTH/3 - 10)/2), SCREEN_HEIGHT - 380, (SCREEN_WIDTH/3 - 10)/2 - 15, 175, "Attack 2", 120, colour = "white", visible = True)
    player_attack_3_b = Text(20, SCREEN_HEIGHT - 195, (SCREEN_WIDTH/3 - 10)/2 - 15, 175, "Attack 3", 120, colour = "white", visible = True)
    player_attack_4_b = Text(15 + ((SCREEN_WIDTH/3 - 10)/2), SCREEN_HEIGHT - 195, (SCREEN_WIDTH/3 - 10)/2 - 15, 175, "Attack 4", 120, colour = "white", visible = True)

    enemy_attacks_b = Rectangle(SCREEN_WIDTH*2/3, SCREEN_HEIGHT - 390, SCREEN_WIDTH/3 - 10, 380, "red", True)
    enemy_attack_1_b = Text(SCREEN_WIDTH*2/3 + 10, SCREEN_HEIGHT - 380, (SCREEN_WIDTH/3 - 10)/2 - 15, 175, "Attack 1", 120, colour = "white", visible = True)
    enemy_attack_2_b = Text(SCREEN_WIDTH*2/3 + 5 + ((SCREEN_WIDTH/3 - 10)/2), SCREEN_HEIGHT - 380, (SCREEN_WIDTH/3 - 10)/2 - 15, 175, "Attack 2", 120, colour = "white", visible = True)
    enemy_attack_3_b = Text(SCREEN_WIDTH*2/3 + 10, SCREEN_HEIGHT - 195, (SCREEN_WIDTH/3 - 10)/2 - 15, 175, "Attack 3", 120, colour = "white", visible = True)
    enemy_attack_4_b = Text(SCREEN_WIDTH*2/3 + 5 + ((SCREEN_WIDTH/3 - 10)/2), SCREEN_HEIGHT - 195, (SCREEN_WIDTH/3 - 10)/2 - 15, 175, "Attack 4", 120, colour = "white", visible = True)


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