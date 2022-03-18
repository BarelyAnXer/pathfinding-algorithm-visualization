import pygame
from pygame import *
pygame.init()

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()


# window.fill((255,255,255))
BLACK = (0, 0, 0)

no_of_row = 30
no_of_columns = 30

cell_width = int(WINDOW_WIDTH / no_of_columns)
cell_height = int(WINDOW_HEIGHT / no_of_row)

all_cell = []

border = 1

for row in range(no_of_row): 
    items = []
    for column in range(no_of_columns):
        rect  = pygame.Rect(column * cell_width, row * cell_height, cell_width - border, cell_height - border)
        color = (13, 152, 186)
        items.append([rect,color])  
    all_cell.append(items)


running = True
while running:

        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
        

        if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            mousepressed = pygame.mouse.get_pressed()
            for rows in all_cell:
                for cell in rows:
                    # cell[0] = x y width height
                    # cell[1] = rgb color
                    if cell[0].collidepoint(pos) and (1,0,0) == mousepressed:
                        # print(mousepressed)
                        # print(cell[0].center)
                        cell[1] = (149, 0, 255)
                    elif cell[0].collidepoint(pos) and (0,0,1) == mousepressed:
                        cell[1] = (13, 152, 186)
                    
            
    
    
    

    for row in all_cell:
        for cell in row:
            xywh, color = cell
            # print(xywh)

            
            pygame.draw.rect(window,color,(xywh[0], xywh[1], xywh[2], xywh[3]))

    
    
    # clock.tick(5)
    pygame.display.update()