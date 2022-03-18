import pygame
from pygame import *
import pprint
import random

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

BLACK = (0, 0, 0)
WHITE = (255, 255 ,255)


pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
clock = pygame.time.Clock()


cellgrid = []
# defauly number of column & row
dflt_no_row = 3
dflt_no_column = 2



def main():
    global dflt_no_row, dflt_no_column

    # drawGrid()


    running = True
    while running:
        
        window.fill((255,255,255))
        drawGrid(dflt_no_row, dflt_no_column)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    cells = []
                    print("change")
                    dflt_no_row = random.randrange(1,20)
                    dflt_no_column = random.randrange(1,20)
                    drawGrid(dflt_no_row, dflt_no_column)
                    

            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     pos = pygame.mouse.get_pos()
            #     for cell in cells:
            #         for rect in cell:
            #             if rect.collidepoint(pos):
            #                 print(rect[0])

        clock.tick(5)
        pygame.display.update()

def drawGrid(no_of_row = 10, no_of_columns = 10): 

    cell_width = int(WINDOW_WIDTH / no_of_columns)
    cell_height = int(WINDOW_HEIGHT / no_of_row)


    if cell_width == cell_height:
        pass
    elif cell_height < cell_width:
        cell_height = cell_height
        cell_width = cell_height
    elif cell_width < cell_height :
        cell_height = cell_width
        cell_width = cell_width
    
    
    for row in range(no_of_row): 
        items = []
        for column in range(no_of_columns):
            xywh = (column * cell_width, row * cell_height, cell_width, cell_height)
            cell = pygame.draw.rect(window, BLACK, xywh, 1)
            items.append(cell)  
        cellgrid.append(items)
    

    # pprint.pprint(cells)
    # print(cells[0])
    # print(cells[0][0].height)

if __name__ == "__main__":
    main()

