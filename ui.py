import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

pygame.font.init()
FONT = pygame.font.SysFont(None, 24)

class UI:
    def __init__(self):
        self.buttons = []   # List to hold button objects
        self.resource_pos= (10,10)  # Position for resource display
    
    def draw_resources(self, screen, resources):
        """Draw the resources on the screen."""
        resource_text = f"${resources}"
        text_surface = FONT.render(resource_text, True, (255, 255, 255))
        screen.blit(text_surface, self.resource_pos)
    
    def add_buttons(self, react,text,callback):
        """Add a button to the UI."""
        self.buttons.append({
            'react': react,
            'text': text,
            'callback': callback
        })
    def draw_buttons(self, screen):
        """Draw all buttons on the screen."""
        mouse_pos= pygame.mouse.get_pos()
        for button in self.buttons:
            hovered = button['react'].collidepoint(mouse_pos)
            color = (200, 200, 200) if hovered else (150, 150, 150)
            pygame.draw.rect(screen, color, button['react'])
            text_surface = FONT.render(button['text'], True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=button['react'].center)
            screen.blit(text_surface, text_rect)
    
    def handle_events(self, event):
        """Handle events for buttons."""
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
            pos = event.pos
            for button in self.buttons:
                if button['react'].collidepoint(pos):
                    button['callback']()  # Call the button's callback function