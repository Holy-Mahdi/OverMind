import pygame
from settings import *
from ui import UI

ui = UI()

def build_barracks():
    print("Building Barracks...")

ui.add_buttons(pygame.Rect(10, 50, 100, 30), "Build Barracks", build_barracks)
ui.add_buttons(pygame.Rect(10, 90, 100, 30), "Train Unit", lambda: print("Training Unit..."))



pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("OverMind - a RTS game")
clock = pygame.time.Clock()


running = True
while running:
    for event in pygame.event.get():
        ui.handle_events(event)
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))
    ui.draw_resources(screen, 100)  # Example resource count
    ui.draw_buttons(screen)  # Draw buttons on the screen  

    # Here you would typically update game state and draw everything
    pygame.display.flip()
    clock.tick(FPS) 

pygame.quit()
exit(0)