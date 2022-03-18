import pygame
from pygame import *


class Cell:
    def __init__(self, state):
        # states = wall, start, end, empty
        
        self.state = state
    
class Maze: 
    
    def __init__(self):
        self.BLACK = (0, 0, 0)
        self.GREEN = (0, 255 ,0)
        self.RED = (255, 0, 0)
        self.WHITE = (255,255,255)

        self.border_width = 1

        self.no_of_rows = 10
        self.no_of_columns = 10
        # bawal zero

        self.WINDOW_WIDTH = 700
        self.WINDOW_HEIGHT = 700
        
        self.cell_height = int(self.WINDOW_HEIGHT / self.no_of_rows)
        self.cell_width = int(self.WINDOW_WIDTH / self.no_of_columns)

        self.maze = []
        self.running =  True

    def on_init(self):
        pygame.init()
        pygame.display.set_caption("Visualize")
        self.window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))

    def generate_grid(self):
        if self.cell_width == self.cell_height:
            pass
        elif self.cell_height < self.cell_width:
            self.cell_height = self.cell_height
            self.cell_width = self.cell_height
        elif self.cell_width < self.cell_height :
            self.cell_height = self.cell_width
            self.cell_width = self.cell_width

        for rows in range(self.no_of_rows):
            nodes = []
            for node in range(self.no_of_columns):
                rect = pygame.Rect(node * self.cell_width, rows * self.cell_height, self.cell_width - self.border_width, self.cell_height - self.border_width)
                nodes.append([rect, self.WHITE])
            self.maze.append(nodes)

    # def draw_start_end:

    def find(self, maze, node):
        for index, value in enumerate(maze):
            if node in value:
                return (index, value.index(node))   

    def draw_generated_grid(self):

        for rows in self.maze:
            for node in rows:
                xywh, color = node

                # tenp generation ng start and end ibahin mamaya para automatic
                # sa pag genrate ng wall ng maze
                # automatic na to na mapleplace sa (0,0) and (maze[-1],maze[-1][-1])
                # lagay mo sa function na draw_start end sa taas
                if self.find(self.maze, node) == (0,0):
                    x,y = self.find(self.maze, node)
                    self.maze[x][y][1] = self.RED
                    pygame.draw.rect(self.window, self.RED, xywh)
                    continue
                elif self.find(self.maze, node) == (len(self.maze) - 1, len(self.maze[0]) - 1):
                    x,y = self.find(self.maze, node)
                    self.maze[x][y][1] = self.GREEN
                    pygame.draw.rect(self.window, self.GREEN, xywh)
                    continue    


                pygame.draw.rect(self.window, color, xywh) 
                # try to change later to xywh only

    def mainloop(self):
        self.generate_grid()
        self.draw_generated_grid()
        self.selected = None

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False 

                if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONDOWN:
                    mousex, mousey = pygame.mouse.get_pos()
                    mouse_button_pressed = pygame.mouse.get_pressed()
                    for rows in self.maze:
                        for node in rows:
                            xywh, color = node
                            # xywh is also the rect class / object? xywh is Rect()
                            if xywh.collidepoint((mousex, mousey)) and (1,0,0) == mouse_button_pressed:
                                
                                if color == self.RED or color == self.GREEN:
                                    if event.type == pygame.MOUSEBUTTONDOWN:# and color or state == red and start or green and end 
                                        if xywh.collidepoint((mousex, mousey)):
                                            selected = xywh
                                    if event.type == pygame.MOUSEBUTTONUP:
                                        selected = None
                                    elif event.type == pygame.MOUSEMOTION:
                                        if selected is not None:
                                            node[0] = pygame.Rect(mousex, mousey ,xywh.w, xywh.h)
                                            pygame.draw.rect(self.window, self.RED, node[0])
                                else:
                                    x, y = self.find(self.maze, node)
                                    color = self.BLACK
                                    self.maze[x][y][1] = self.BLACK
                                    pygame.draw.rect(self.window,self.BLACK,xywh)

                            elif xywh.collidepoint((mousex, mousey)) and (0,0,1) == mouse_button_pressed:
                                if color == self.BLACK:
                                    x, y = self.find(self.maze, node)
                                    self.maze[x][y][1] = self.WHITE
                                    pygame.draw.rect(self.window,self.WHITE,xywh)
                

            
        
            pygame.display.flip()
        
        # print(self.maze)

if __name__ == "__main__":
    maze = Maze()
    maze.on_init()
    maze.mainloop()
    