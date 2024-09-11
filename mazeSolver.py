import random

# Constants to represent the maze structure
WALL = '#'
PATH = ' '
START = 'S'
GOAL = 'G'

# Directions for movement in the maze (moving by 2 cells at a time)
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[WALL for _ in range(width)] for _ in range(height)]
        self.start = (1, 1)
        self.end = (height - 2, width - 2)
        self.grid[self.start[0]][self.start[1]] = START
        self.grid[self.end[0]][self.end[1]] = GOAL
        self.generate_maze(self.start[0], self.start[1])

    def generate_maze(self, row, col):
        neighbors = self.get_neighbors(row, col)
        random.shuffle(neighbors)  # Randomize neighbors to avoid bias in path generation
        
        for next_row, next_col in neighbors:
            if self.grid[next_row][next_col] == self.grid[self.end[0]][self.end[1]]:
                print('goal')
                return
            if self.grid[next_row][next_col] == WALL and self.openNeighbors(next_row, next_col) < 2:  # Ensure less than 1 open neighbors
                self.grid[next_row][next_col] = PATH
                self.generate_maze(next_row, next_col)

    def prettyPrint(self):
        caps = '-' * self.width * 2 + '--'
        print(caps)
        for row in self.grid:
            line = "|"
            for col in row:
                line += col + ' '
            line += "|"
            print(line)
        print(caps)

    def get_neighbors(self, row, col):
        neighbors = []
        if(row > 0):
            neighbors.append((row-1, col))
        if(col > 0):
            neighbors.append((row, col-1))
        if(col < self.width-1):
            neighbors.append((row, col+1))
        if(row < self.height-1):
            neighbors.append((row+1, col))
        return neighbors

    def openNeighbors(self, row, col):
        numOpen = 0
        for next_row, next_col in self.get_neighbors(row, col):
            if self.grid[next_row][next_col] == PATH:
                numOpen += 1
        return numOpen

class AStarAgent:
    __init__

# Example of generating a 10x10 maze
maze = Maze(20, 20)
maze.prettyPrint()
