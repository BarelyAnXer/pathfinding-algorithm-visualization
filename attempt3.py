import pygame
from pygame import *
from pygame.locals import *
from math import ceil

RED = (255, 0, 0)
GREEN = (0, 255 ,0)
BLACK = (0, 0, 0)
WHITE = (255,255,255)
DARKBLUE = (30, 0, 255)
LIGHTBLUE = (0, 247, 255)


class Cell:
    
    def __init__(self, color, x, y, width, height):
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.parent = None

        # state wall empty start end
        self.color = color

        self.parent = None
        # self.visited = False or make list of visited in Maze class


class StackFrontier:
    def __init__(self):
        self.frontier = []
    
    def add(self, cell):
        self.frontier.append(cell)
    
    def is_empty(self):
        return len(self.frontier) > 0

    def remove(self):
        cell = self.frontier[-1]
        self.frontier = self.frontier[:-1]
        return cell

class QueueFrontier(StackFrontier):
    def remove(self):
        cell = self.frontier[0]
        self.frontier = self.frontier[1:]
        return cell

class Maze:
    def __init__(self,no_of_rows = 3, no_of_columns = 3):
        self.border_width = 1

        self.no_of_rows = no_of_rows
        self.no_of_columns = no_of_columns
        # bawal zero

        self.WINDOW_WIDTH = 700
        self.WINDOW_HEIGHT = 700
        
        self.cell_height = ceil(self.WINDOW_HEIGHT / self.no_of_rows)
        self.cell_width = ceil(self.WINDOW_WIDTH / self.no_of_columns)

        self.grid = []
        self.running =  True
        
        self.frontier = None
        self.explored = set()

    def find_neighbors(self, cell):
        neighbors = []
        # moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        moves = [(0, -1), (1, 0), (0, 1), (-1, 0)] # reversed
        # moves = [(-1, 0), (0, 1), (1, 0), (0, -1),  (-1, -1), (-1, 1), (1, 1), (1, -1)]
        # moves = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

        # TODO i think the problem is dun sa explored parang di na sila bumabal;ik
        # run mo yung pangalawang moves para makita mo sa iba hindi masyado eh 

        x, y = self.find_index_2d(cell)
        
        if cell.color == WHITE: # pwede to alisin
            pygame.draw.rect(self.window, DARKBLUE, cell.rect)
        
        for i, j in moves:
            # check if the next neighbor exist (out of bounds) outside of the given rows and columns
            if ((x + i) >= 0 and (y + j) >= 0) and ((x + i) < len(self.grid) and (y + j) < len(self.grid[0])):
                # check if it is not a start or wall
                if self.grid[x + i][y + j].color == WHITE or self.grid[x + i][y + j].color == GREEN:
                    # checks if the neighbor is both not in frontier and expored then we can add them
                    if self.grid[x+i][y+j] not in self.frontier.frontier and self.grid[x+i][y+j] not in self.explored:
                        self.grid[x+i][y+j].parent = self.grid[x][y]
                        neighbors.append(self.grid[x+i][y+j])
                        self.frontier.add(self.grid[x+i][y+j])

        for neighbor in neighbors:
            if neighbor.color == GREEN:
                continue
            pygame.draw.rect(self.window, LIGHTBLUE, neighbor.rect)
            pygame.display.update()         
            pygame.time.delay(100)

    def depth_first_search(self):
        explored = 0
        self.frontier = StackFrontier()
        sol = []

        #  to determine where is the start dynamically 
        for rows in self.grid:
            for cell in rows:
                if cell.color == RED:
                    self.frontier.add(cell) 

        while True:
            if len(self.frontier.frontier) == 0:
                print("no solution")
                break
            
            cell = self.frontier.remove()
            explored += 1
            if cell.color == GREEN:
                print("solution")
                while cell.parent is not None:
                    sol.append(cell)
                    cell = cell.parent
                break

            self.explored.add(cell)

            self.find_neighbors(cell)
        


        for i in self.grid:
            for j in i:
                print(j.parent)
        for i in sol:
            if i.color is not GREEN:
                pygame.draw.rect(self.window,(123,123,132),i.rect)
        print(explored)



        self.frontier.frontier.clear()
  

    def breadth_first_search(self):
        sol = []
        explored = 0
        self.frontier = QueueFrontier()
        
        for rows in self.grid:
            for cell in rows:
                if cell.color == RED:
                    self.frontier.add(cell) 

        while True:
            if len(self.frontier.frontier) == 0:
                print("no solution")
                break
            
            cell = self.frontier.remove()
    
            if cell.color == GREEN:
                print("solution")
                while cell.parent is not None:
                    sol.append(cell)
                    cell = cell.parent
                break

            self.explored.add(cell)

            self.find_neighbors(cell)
        

        for i in self.grid:
            for j in i:
                print(j.parent)
        for i in sol:
            if i.color is not GREEN:
                pygame.draw.rect(self.window,(123,123,132),i.rect)
        print(explored)



        self.frontier.frontier.clear()

    def on_init(self):
        pygame.init()
        pygame.display.set_caption("Visualize")
        self.window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()

    def generate_grid(self):
        if self.cell_width == self.cell_height:
            pass
        elif self.cell_height < self.cell_width:
            self.cell_height = self.cell_height
            self.cell_width = self.cell_height
        elif self.cell_width < self.cell_height:
            self.cell_height = self.cell_width
            self.cell_width = self.cell_width

        for x in range(self.no_of_rows):
            cells = []
            for y in range(self.no_of_columns):
                # creating start and end
                if x == 0 and y == 0:
                    cell = Cell(RED, y * self.cell_width, x * self.cell_height, self.cell_width - self.border_width, self.cell_height - self.border_width)
                    cells.append(cell)
                    continue

                if x == self.no_of_rows - 1 and y == self.no_of_columns - 1:
                    cell = Cell(GREEN, y * self.cell_width, x * self.cell_height, self.cell_width - self.border_width, self.cell_height - self.border_width)
                    cells.append(cell)
                    continue

                cell = Cell(WHITE, y * self.cell_width, x * self.cell_height, self.cell_width - self.border_width, self.cell_height - self.border_width)
                cells.append(cell)
            self.grid.append(cells)

    def draw_generated_grid(self):
        for rows in self.grid:
            for cell in rows:
                pygame.draw.rect(self.window, cell.color, cell.rect)
    
    def is_click_valid(self, mousex, mousey):
        """checks if mouse click is inside the grid returns true if its is inside and false if outside """
        if mousex < (self.no_of_columns * self.cell_width) and mousey < (self.no_of_rows * self.cell_height):
            return True
        return False

    def find_index_2d(self, cell):
        for index, row_value in enumerate(self.grid):
            if cell in row_value:
               return index, row_value.index(cell)

    def mainloop(self):
        self.generate_grid()
        self.draw_generated_grid()
        selected = None


        while self.running:
            mousex, mousey = pygame.mouse.get_pos()
            x = mousey // self.cell_width
            y =  mousex // self.cell_height
            
            
            """
            press 
            q for depth first search
            w for breadth first search

            c to clear the walls or to clear the maze after search 
            """
            for event in pygame.event.get():
                mouse_button_pressed = pygame.mouse.get_pressed()
                if event.type == pygame.QUIT:
                    self.running = False 
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.depth_first_search()            
                    elif event.key == pygame.K_w:
                        self.breadth_first_search()
                    elif event.key == pygame.K_c:
                        for rows in self.grid:
                            for cell in rows:
                                if cell.color == RED or cell.color == GREEN:
                                    continue

                                cell.color = WHITE
                                pygame.draw.rect(self.window, WHITE, cell.rect)

                        self.explored.clear()
                            
                         
            
                if event.type == MOUSEBUTTONDOWN:

                    if self.is_click_valid(mousex, mousey):    

                        cell = self.grid[x][y]
                        # TODO change all to short way event.button
                        if self.grid[x][y].color == RED and mouse_button_pressed == (1,0,0):
                            selected = self.grid[x][y]
                        elif self.grid[x][y].color == GREEN and mouse_button_pressed == (1,0,0):
                            selected = self.grid[x][y]
                        elif self.grid[x][y].color == WHITE and mouse_button_pressed == (1,0,0):
                            selected = self.grid[x][y]
                            self.grid[x][y].color = BLACK
                            pygame.draw.rect(self.window, BLACK, self.grid[x][y].rect)

                            # self.find_neighbors(self.grid[x][y])
                            # delete this later

                        elif self.grid[x][y].color == BLACK and mouse_button_pressed == (0,0,1):
                            selected = self.grid[x][y]
                            self.grid[x][y].color = WHITE
                            pygame.draw.rect(self.window, WHITE, self.grid[x][y].rect)

                if event.type == pygame.MOUSEBUTTONUP:
                    selected = None  

                elif event.type == pygame.MOUSEMOTION:
                    # cell is the currecnt cell na nasa taas ng mouse position 
                    # selected is the cell na mouse button down

                    if selected is not None:

                        if self.is_click_valid(mousex, mousey): 
                            cell = self.grid[x][y]
                            
                            if selected.color == RED or selected.color == GREEN:
                                if selected.color == RED and mouse_button_pressed == (1,0,0):
                                    # check if nag collide yung mouse pos sa ibang rect
                                    if cell.rect.collidepoint((mousex, mousey)):
                                        if cell.color != BLACK and cell.color != GREEN:
                                            # redraw on top of each other
                                            pygame.draw.rect(self.window, WHITE, selected.rect)    
                                            pygame.draw.rect(self.window, RED, cell.rect)
                                            
                                            # swapping the values and the selected 
                                            selected.color, cell.color = cell.color, selected.color
                                            if selected != cell:
                                                pygame.draw.rect(self.window, WHITE, cell.rect)
                                                selected = cell
                                            selected.rect, cell.rect = cell.rect, selected.rect
                                # same as code for red 
                                if selected.color == GREEN and mouse_button_pressed == (1,0,0):
                                    if cell.rect.collidepoint((mousex, mousey)):
                                        if cell.color != BLACK and cell.color != RED:
                                            pygame.draw.rect(self.window, WHITE, selected.rect)    
                                            pygame.draw.rect(self.window, GREEN, cell.rect)
                                            selected.color, cell.color = cell.color, selected.color
                                            if selected != cell:
                                                pygame.draw.rect(self.window, WHITE, cell.rect)
                                                selected = cell
                                            selected.rect, cell.rect = cell.rect, selected.rect

                            elif cell.color == WHITE and mouse_button_pressed == (1,0,0):
                                cell.color = BLACK
                                pygame.draw.rect(self.window, BLACK, cell.rect)
                            elif cell.color == BLACK and mouse_button_pressed == (0,0,1):
                                cell.color = WHITE
                                pygame.draw.rect(self.window, WHITE, cell.rect)              



            pygame.display.flip()        
        
        

if __name__ == "__main__":
    maze = Maze(no_of_rows = 7, no_of_columns = 12)
    maze.on_init()
    maze.mainloop()