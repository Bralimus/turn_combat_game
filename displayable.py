import pygame
from constants import *

class Displayable(pygame.sprite.Sprite):    
    def __init__(self, colour = "white", visible = False):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.colour = colour
        self.visible = visible
        self.alpha = 255
        self.fade_state = "visible"
        self.display_timer = 0
        if self.containers:
            self.containers.add(self)

    def update_fade(self, dt):
        if self.fade_state == "fade_in": #setting .fade_state = "fade_in" starts process
            self.alpha = min(255, self.alpha + (255 * dt))
            if self.alpha == 255:
                self.fade_state = "visible"
                self.display_timer = 0
        elif self.fade_state == "visible":
            self.display_timer += dt
            if self.display_timer >= 2:
                self.fade_state = "fade_out"
        elif self.fade_state == "fade_out":
            self.alpha = max(0, self.alpha - (255 * dt))

class Rectangle(Displayable):
    def __init__(self, x, y, width, height, colour = "white", visible = False):
        super().__init__(colour, visible)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        if colour is None:
            self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        else:
            self.image = pygame.Surface((self.width, self.height))
            self.image.fill(self.colour)

    def update_size(self, new_width=None, new_height=None):
        if new_width is not None:
            self.width = new_width
            self.rect.width = new_width
        if new_height is not None:
            self.height = new_height
            self.rect.height = new_height
        if self.colour is None:
            self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        else:
            self.image = pygame.Surface((self.width, self.height))
            self.image.fill(self.colour)

    def update_position(self, new_x=None, new_y=None):
        if new_x is not None:
            self.x = new_x
            self.rect.x = new_x
        if new_y is not None:
            self.y = new_y
            self.rect.y = new_y


class InputBox(Rectangle):
    def __init__(self, colour, width, height, x, y, visible, font_size, words = ""):
        super().__init__(colour, width, height, x, y, visible)
        self.font_size = font_size
        self.words = words
        self.active = False
        self.font = pygame.font.Font(None, font_size)
        self.colour_inactive = colour
        self.colour_active = GREEN
        
    
    def change_active_status(self, force_active=None):
        if force_active is None:
            self.active = not self.active
        else:
            self.active = force_active
        self.colour = self.colour_active if self.active else self.colour_inactive
        self.image.fill(self.colour)
    
    def handle_event(self, event):
        if self.active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.words = self.words[:-1]
                else:
                    self.words += event.unicode
    
    def draw(self, screen):
        if self.visible:
            screen.blit(self.image, self.rect)
            text_surface = self.font.render(self.words, True, WHITE)
            text_rect = text_surface.get_rect(center=self.rect.center)
            screen.blit(text_surface, text_rect)

    
class Text(Rectangle):
    def __init__(self, x, y, width, height, words, font_size, 
                 words_colour = "black", colour = "white", visible = False):
        super().__init__(x, y, width, height, colour, visible)
        self.font_size = font_size
        self._words = words
        self.words_colour = words_colour
        self.update_text(words)

    def update_text(self, new_words):
        self._words = new_words

        if self.colour is None:
            self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        else:
            self.image = pygame.Surface((self.width, self.height))
            self.image.fill(self.colour)

        wrapped_lines = self.wrap_text(self._words, self.width - 5, self.height - 5)
        font = pygame.font.Font(None, self.font_size)
        
        line_height = font.get_height()
        total_text_height = line_height * len(wrapped_lines)

        start_y = (self.height - total_text_height) // 2

        y_offset = start_y
        for line in wrapped_lines:
            line_surface = font.render(line, True, self.words_colour)
            line_rect = line_surface.get_rect()
            line_rect.centerx = (self.width - 5) // 2
            line_rect.y = y_offset
            self.image.blit(line_surface, line_rect)
            y_offset += font.get_height()

    def wrap_text(self, text, max_width, max_height):
        words = text.split()
        current_font_size = self.font_size
        current_font = pygame.font.Font(None, current_font_size)

        for word in words:
            word_width = current_font.size(word)[0]
            while word_width > max_width:
                current_font_size -= 1
                current_font = pygame.font.Font(None, current_font_size)
                word_width = current_font.size(word)[0]
        
        while True:
            words = text.split(' ')
            lines = []
            current_line = []

            current_font = pygame.font.Font(None, current_font_size)
            
            for word in words:
                current_line.append(word)
                test_line = ' '.join(current_line)
                width = current_font.size(test_line)[0]
                
                if width > max_width:
                    current_line.pop()
                    if current_line:
                        lines.append(' '.join(current_line))
                    current_line = [word]
            
            if current_line:
                lines.append(' '.join(current_line))
            
            total_height = len(lines) * current_font.get_height()
            if total_height <= max_height or current_font_size <= 20:
                break

            current_font_size -= 5

        self.font_size = current_font_size
        return lines