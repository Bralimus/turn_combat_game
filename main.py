#Beginning Turn Based Combat Game
#      cd ~/workspace/github.com/Bralimus/turn_combat_game
#   https://pygame-menu.readthedocs.io/en/latest/
import pygame
from menus import GameMenus
from constants import *
from displayable import Displayable, Rectangle, Text
from battle_actions import BattleScreen

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0

    drawable = pygame.sprite.Group()

    Displayable.containers = (drawable)
    
    battle = BattleScreen()
    menus = GameMenus(battle)

    print("Starting Game")

    while True:
        dt = clock.tick(60)/1000
        events = pygame.event.get()
        mouse_pos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if menus.is_playing:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        menus.toggle_pause() #add game pause to this to stop click through
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (battle.attack.rect.collidepoint(mouse_pos) and
                        battle.attack.visible == True):
                        battle.use_attack()
                        battle.next_turn()
                    battle.check_all_attack_buttons(mouse_pos)
                    
        
        battle.new_turn_background.update_fade(dt)
        battle.new_turn.update_fade(dt)
        battle.attack_info_()


        if menus.is_playing:
            screen.fill("cyan")
            if battle.player_1.current_hp <= 0 or battle.player_2.current_hp <= 0:
                for sprite in drawable:
                    if sprite in vars(battle).values():
                        sprite.visible = False
                if battle.player_1.current_hp <= 0:
                    menus.winner = battle.player_2.name
                else:
                    menus.winner = battle.player_1.name
                menus.end_game()
            for sprite in drawable:
                if sprite.visible:
                    sprite.image.set_alpha(sprite.alpha)
                    screen.blit(sprite.image, sprite.rect)

        if menus.current_menu.is_enabled():
            menus.current_menu.draw(screen)
            menus.current_menu.update(events)


        pygame.display.flip()
        

if __name__ == "__main__":
    main()