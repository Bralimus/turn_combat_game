import pygame_menu
from constants import *


class GameMenus:
    def __init__(self, battle):
        self.battle = battle
        self.main_menu = pygame_menu.Menu('New Game', SCREEN_WIDTH, SCREEN_HEIGHT,
                                theme = pygame_menu.themes.THEME_SOLARIZED)
        self.pause_menu = pygame_menu.Menu('Pause', SCREEN_WIDTH - 100, SCREEN_HEIGHT - 100, 
                                theme = pygame_menu.themes.THEME_DARK)
        self.end_menu = pygame_menu.Menu('End of Game', SCREEN_WIDTH, SCREEN_HEIGHT,
                                theme = pygame_menu.themes.THEME_SOLARIZED)

        self.setup_main_menu()
        self.setup_pause_menu()
        self.current_menu = self.main_menu
        self.is_playing = False
        self.winner = None
    
    def setup_main_menu(self):
        self.main_menu.add.text_input('Name: ', default = 'Bralimus', font_size = 75, margin = (0,50))
        self.main_menu.add.selector('Players', [('1',1), ('2',2)], font_size = 75, margin = (0,50))
        self.main_menu.add.button('Play', self.disable_menus, font_size = 75, margin = (0,50))
        self.main_menu.add.button('Quit', pygame_menu.events.EXIT, font_size = 75, margin = (0,50))
   
    
    def setup_pause_menu(self):
        self.pause_menu.add.button('Resume', self.toggle_pause, font_size = 75, margin = (0,50))
        self.pause_menu.add.button('Quit', pygame_menu.events.EXIT, font_size = 75, margin = (0,50))        


    def toggle_pause(self):
        if self.current_menu == self.pause_menu:
            self.pause_menu.disable()
            self.current_menu = self.main_menu
        else:
            self.pause_menu.enable()
            self.current_menu = self.pause_menu

    def disable_menus(self):
        self.current_menu.disable()
        self.is_playing = True
        self.battle.next_turn()

    def end_game(self):
        self.end_menu.add.label(f'The winner is {self.winner}', font_size = 75)
        self.end_menu.add.button('Quit', pygame_menu.events.EXIT, font_size = 75, margin = (0, 50))
        self.is_playing = False
        self.current_menu = self.end_menu
        self.end_menu.enable()
