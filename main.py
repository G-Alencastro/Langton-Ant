

class Ant:
    def __init__(self, pos=[50, 50], grid_size=(100, 100)):
        self.grid = [[0 for _ in range(grid_size[0])] for _ in range(grid_size[1])]
        self.pos = pos
        self.actual_dir = 0

    def walk(self):
        directions = (0, 1), (1, 0), (0, -1), (-1, 0)
        actual_color = self.grid[self.pos[0]][self.pos[1]]
        
        if actual_color == 0:
            self.grid[self.pos[0]][self.pos[1]] = 1
            self.actual_dir += -1 if self.actual_dir > 0 else 3

        if actual_color == 1:
            self.grid[self.pos[0]][self.pos[1]] = 2
            self.actual_dir += -1 if self.actual_dir > 0 else 3
        
        if actual_color == 2:
            self.grid[self.pos[0]][self.pos[1]] = 3
            self.actual_dir += 1 if self.actual_dir < 3 else -3

        if actual_color == 3:
            self.grid[self.pos[0]][self.pos[1]] = 0
            self.actual_dir += 1 if self.actual_dir < 3 else -3

            
        self.pos[0] += directions[self.actual_dir][0]
        self.pos[1] += directions[self.actual_dir][1]

if __name__  == '__main__':
    ant = Ant([50, 50])

    for step in range(100):
        print(step)
        ant.walk()

