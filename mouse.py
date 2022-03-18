import pygame

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700



pygame.init()
pygame.display.set_caption("Visualize")
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

running = True
while running:
    for event in pygame.event.get():
        mouse_button_pressed = pygame.mouse.get_pressed()
        if event.type == pygame.QUIT:
            running = False 

        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if event.type == pygame.MOUSEMOTION:
                print("123")