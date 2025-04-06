class Node:
    def __init__(self, x, y, depth):
        self.x = x
        self.y = y
        self.depth = depth


class IDDFS:
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.N = len(grid)
        self.M = len(grid[0])
        self.start = Node(start[0], start[1], 0)
        self.goal = Node(goal[0], goal[1], float('inf'))
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up=x+, down=x-, left=y-, right=y+
        self.path = []
        self.found = False

    def is_valid(self, x, y, visited):
        return 0 <= x < self.N and 0 <= y < self.M and self.grid[x][y] == 0 and not visited[x][y]

    def depth_limited_search(self, node, depth_limit, visited, path):
        x, y, depth = node.x, node.y, node.depth

        if depth > depth_limit:
            return False

        if (x, y) == (self.goal.x, self.goal.y):
            self.path = path + [(x, y)]
            self.goal.depth = depth
            return True

        visited[x][y] = True
        path.append((x, y))

        for dx, dy in self.directions:
            nx, ny = x + dx, y + dy
            if self.is_valid(nx, ny, visited):
                next_node = Node(nx, ny, depth + 1)
                if self.depth_limited_search(next_node, depth_limit, visited, path.copy()):
                    return True

        return False

    def iddfs(self, max_depth_limit=100):
        for depth in range(max_depth_limit):
            visited = [[False] * self.M for _ in range(self.N)]
            self.path = []
            if self.depth_limited_search(self.start, depth, visited, []):
                print(f"\nPath found at depth {self.goal.depth} using IDDFS")         
                print("Traversal Order:", self.path)
                return
        print(f"\nPath not found at max depth {max_depth_limit} using IDDFS")
        
def main():
    rows, cols = map(int, input().split())
 
    grid = [[0] * cols for _ in range(rows)] 
    for x in range(cols):
        col_values = list(map(int, input().split()))
        for y in range(rows):
            grid[y][x] = col_values[y]
    
    print("Start:", end=" ")
    start_x, start_y = map(int, input().split())

    print("Target:", end=" ")
    goal_x, goal_y = map(int, input().split())

    solver = IDDFS(grid, (start_x, start_y), (goal_x, goal_y))
    solver.iddfs()


if __name__ == "__main__":
    main()