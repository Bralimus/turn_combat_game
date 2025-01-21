import random
import pygame
from constants import *
from displayable import Displayable, Rectangle, Text
from units import Player, Attack

class BattleScreen:
    def __init__(self):
        #Attack Options
        self.attack_1 = Attack("Hit", 10, 
                               "Hit the target as hard as you can dealing damage. (20)") #Will add dmg display and type
        self.attack_2 = Attack("Punch", 0, 
                               "Punch the target doing some damage. (10)")
        self.attack_3 = Attack("Block", -10, 
                               "Block taking no damage from your opponent this turn. (0)") #Add immunity
        self.attack_4 = Attack("Heal", -20, 
                               "Heal yourself increasing your current health. (+15)") #Add self targeting
        self.attacks = [self.attack_1, self.attack_2, self.attack_3, self.attack_4]
        
        #Players
        self.player_1 = Player("Bralimus") #Will take input for this later
        self.player_2 = Player("Theo")
        self.players = [self.player_1.name, self.player_2.name]

        self.header_b = Text(SCREEN_WIDTH/2 - 300, 0, 600, 100, "Battle!", 120, visible = True)
        self.menu_button_b = Text(0, 0, 150, 70, "Menu", 80, colour = None, visible = True)
        self.help_button_b = Text(SCREEN_WIDTH - 100, 0, 150, 70, "?", 80, colour = None, visible = True)

        self.player_1_sprite = Rectangle(SCREEN_WIDTH/3 - 200, SCREEN_HEIGHT/3 - 50, 400, 400, "blue", True)
        self.player_1_name = Text(SCREEN_WIDTH/3 - 250, 180, 300, 80, self.player_1.name, 100, "white", "black", True)
        self.player_1_hp_border = Rectangle(SCREEN_WIDTH/3 - 250, 250, 500, 100, "black", True)
        self.player_1_hp = Rectangle(SCREEN_WIDTH/3 - 240, 260, 480 * self.player_1.current_hp/self.player_1.max_hp, 80, "green", True) #change size based on %hp
        self.player_1_hp_number = Text(SCREEN_WIDTH/3 - 240, 260, 480, 80, 
                                f"HP: {self.player_1.current_hp}/{self.player_1.max_hp}", #will change based on damage taken and max hp stat
                                100, "white", None, True)

        self.player_2_sprite = Rectangle(SCREEN_WIDTH*2/3 - 200, SCREEN_HEIGHT/3 - 50, 400, 400, "magenta", True)
        self.player_2_name = Text(SCREEN_WIDTH*2/3 - 250, 180, 300, 80, self.player_2.name, 100, "white", "black", True)
        self.player_2_hp_border = Rectangle(SCREEN_WIDTH*2/3 - 250, 250, 500, 100, "black", True)
        self.player_2_hp = Rectangle(SCREEN_WIDTH*2/3 - 240, 260, 480 * self.player_2.current_hp/self.player_2.max_hp, 80, "green", True) #change size based on %hp
        self.player_2_hp_number = Text(SCREEN_WIDTH*2/3 - 240, 260, 480, 80, 
                            f"HP: {self.player_2.current_hp}/{self.player_2.max_hp}", #will change based on damage taken and max hp stat
                            100, "white", None, True)
        
        self.bottom_bar = Rectangle(0, SCREEN_HEIGHT - 400, SCREEN_WIDTH, 400, "black", True)
        self.attack_info_background = Rectangle(SCREEN_WIDTH/3 + 10, SCREEN_HEIGHT - 390, SCREEN_WIDTH/3 - 20, 380, 
                                            "cyan", #will be player colour slightly faded once shift is updated
                                            True)

        self.player_1_attacks_background = Rectangle(10, SCREEN_HEIGHT - 390, SCREEN_WIDTH/3 - 10, 380, "blue", True)
        self.player_1_attack_1 = Text(20, SCREEN_HEIGHT - 380, (SCREEN_WIDTH/3 - 10)/2 - 15, 175, f"{self.attack_1.name}", 120, colour = "white", visible = True)
        self.player_1_attack_2 = Text(15 + ((SCREEN_WIDTH/3 - 10)/2), SCREEN_HEIGHT - 380, (SCREEN_WIDTH/3 - 10)/2 - 15, 175, f"{self.attack_2.name}", 120, colour = "white", visible = True)
        self.player_1_attack_3 = Text(20, SCREEN_HEIGHT - 195, (SCREEN_WIDTH/3 - 10)/2 - 15, 175, f"{self.attack_3.name}", 120, colour = "white", visible = True)
        self.player_1_attack_4 = Text(15 + ((SCREEN_WIDTH/3 - 10)/2), SCREEN_HEIGHT - 195, (SCREEN_WIDTH/3 - 10)/2 - 15, 175, f"{self.attack_4.name}", 120, colour = "white", visible = True)
        self.p1_attack_buttons = [self.player_1_attack_1, self.player_1_attack_2, self.player_1_attack_3, self.player_1_attack_4]

        self.player_2_attacks_background = Rectangle(SCREEN_WIDTH*2/3-10, SCREEN_HEIGHT - 390, SCREEN_WIDTH/3 - 10, 380, "magenta", True)
        self.player_2_attack_1 = Text(SCREEN_WIDTH*2/3 + 10, SCREEN_HEIGHT - 380, (SCREEN_WIDTH/3 - 10)/2 - 15, 175, f"{self.attack_1.name}", 120, colour = "white", visible = True)
        self.player_2_attack_2 = Text(SCREEN_WIDTH*2/3 + 5 + ((SCREEN_WIDTH/3 - 10)/2), SCREEN_HEIGHT - 380, (SCREEN_WIDTH/3 - 10)/2 - 15, 175, f"{self.attack_2.name}", 120, colour = "white", visible = True)
        self.player_2_attack_3 = Text(SCREEN_WIDTH*2/3 + 10, SCREEN_HEIGHT - 195, (SCREEN_WIDTH/3 - 10)/2 - 15, 175, f"{self.attack_3.name}", 120, colour = "white", visible = True)
        self.player_2_attack_4 = Text(SCREEN_WIDTH*2/3 + 5 + ((SCREEN_WIDTH/3 - 10)/2), SCREEN_HEIGHT - 195, (SCREEN_WIDTH/3 - 10)/2 - 15, 175, f"{self.attack_4.name}", 120, colour = "white", visible = True)
        self.p2_attack_buttons = [self.player_2_attack_1, self.player_2_attack_2, self.player_2_attack_3, self.player_2_attack_4] 
        
        self.selected_attack = None
        self.attack_info = Text(SCREEN_WIDTH/3 + 20, SCREEN_HEIGHT - 300, SCREEN_WIDTH/3 - 40, 200, 
                            "Will display information about the attack, what it does and update based on attack selected", 120,
                            colour = None, visible = True)
        self.attack_name = Text(SCREEN_WIDTH/2 - 115, SCREEN_HEIGHT - 380, 230, 70, "Attack 1", 120, visible = True)
        self.attack_border = Rectangle(SCREEN_WIDTH/2 - 125, SCREEN_HEIGHT - 100, 250, 80, visible = True)
        self.attack = Text(SCREEN_WIDTH/2 - 115, SCREEN_HEIGHT - 90, 230, 60, "Attack", 120, colour = "red", visible = True)

        self.turn = None
        self.first_turn = True
        self.new_turn_background = Rectangle(SCREEN_WIDTH/2 - 500, SCREEN_HEIGHT/2 - 250, 1000, 500, "black", True)
        self.new_turn = Text(SCREEN_WIDTH/2 - 450, SCREEN_HEIGHT/2 - 200, 900, 400, f"{self.turn} it's your turn", 120, visible = True)
        self.new_turn_background.alpha = 0
        self.new_turn.alpha = 0

        
        
    def next_turn(self):
        if self.first_turn == True:
            self.turn = random.choice(self.players)
        match self.turn:
            case self.player_1.name: #player_2's turn
                self.turn = self.player_2.name
                self.new_turn.update_text(f"{self.player_2.name} it's your turn")
                self.new_turn_background.alpha = 0
                self.new_turn.alpha = 0
                self.new_turn_background.fade_state = "fade_in"
                self.new_turn.fade_state = "fade_in"
                self.player_2_attacks_background.update_position(SCREEN_WIDTH/3 + 10)
                self.player_2_attacks_background.update_size(SCREEN_WIDTH*2/3 - 20)
                self.player_1_attacks_background.update_size(SCREEN_WIDTH/3 - 10)
                self.selected_attack = None
                self.first_turn = False
            case self.player_2.name: #player_1's turn
                self.turn = self.player_1.name
                self.new_turn.update_text(f"{self.player_1.name} it's your turn")
                self.new_turn_background.alpha = 0
                self.new_turn.alpha = 0
                self.new_turn_background.fade_state = "fade_in"
                self.new_turn.fade_state = "fade_in"
                self.player_1_attacks_background.update_size(SCREEN_WIDTH*2/3 - 20)
                self.player_2_attacks_background.update_position(SCREEN_WIDTH*2/3)
                self.player_2_attacks_background.update_size(SCREEN_WIDTH/3 - 10)
                self.selected_attack = None
                self.first_turn = False


    def check_all_attack_buttons(self, mouse_pos):
        if self.turn == self.player_1.name:
            current_buttons = self.p1_attack_buttons
        else:
            current_buttons = self.p2_attack_buttons
        for button, attack in zip(current_buttons, self.attacks):
            if button.rect.collidepoint(mouse_pos):
                self.selected_attack = attack


    def attack_info_(self):
        if self.selected_attack is None:
            self.attack_info.update_text("")
            self.attack_name.visible = False
            self.attack_border.visible = False
            self.attack.visible = False
        else:
            self.attack_info.update_text(f"{self.selected_attack.info}")
            self.attack_name.update_text(f"{self.selected_attack.name}")
            self.attack_name.visible = True
            self.attack_border.visible = True
            self.attack.visible = True
    
    def use_attack(self):
        if self.turn == self.player_1.name:
            self.player_2.current_hp -= self.selected_attack.calculate_damage(self.player_1.atk)
            self.player_2_hp_number.update_text(f"HP: {self.player_2.current_hp}/{self.player_2.max_hp}")
            self.player_2_hp.update_size(480 * self.player_2.current_hp/self.player_2.max_hp)
        if self.turn == self.player_2.name:
            self.player_1.current_hp -= self.selected_attack.calculate_damage(self.player_2.atk)
            self.player_1_hp_number.update_text(f"HP: {self.player_1.current_hp}/{self.player_1.max_hp}")
            self.player_1_hp.update_size(480 * self.player_1.current_hp/self.player_1.max_hp)

