class MappingAdapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def lighten(self, grid):
        lights = []
        obstacles = []
        self.adaptee.set_dim((len(grid[0]), len(grid)))
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                if grid[j][i] == 1:
                    lights.append((i, j))
                elif grid[j][i] == -1:
                    obstacles.append((i, j))
        self.adaptee.set_lights(lights)
        self.adaptee.set_obstacles(obstacles)
        return self.adaptee.generate_lights()

