import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, name):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.name = name
        self.max_hp = 100
        self.armor = 0
        self.atk = 10
        self.current_hp = self.max_hp
        self.attacks = []

    def add_attack(self, attack):
        self.attacks.append(attack)
    
class Attack:
    def __init__(self, name, base_damage, info):
        self.name = name
        self.base_damage = base_damage
        self.info = info

    def calculate_damage(self, player_atk):
        return self.base_damage + player_atk
        