import numpy as ny


class Node:
    def __init__(self, a, b, z):
        self.x = a
        self.y = b
        self.depth = z

class DFS:
    def __init__(self):
        self.directions = 4
        self.x_move = [1, -1, 0, 0]
        self.y_move = [0, 0, 1, -1]
        self.found = False
        self.N = 0
        self.source = None
        self.goal = None
        self.goal_level = 999999
        self.state = 0

    def init(self):   #-------
        while True:
            #N = int(input("Enter the N value:"))
            N = ny.random.randint(4,8)
            print("The Grid size : ",N)
            # graph = [
            #     [0, 0, 1, 0, 1],
            #     [0, 1, 1, 1, 1],
            #     [0, 1, 0, 0, 1],
            #     [1, 1, 0, 1, 1],
            #     [1, 0, 0, 0, 1]
            # ]
            graph = ny.random.randint(0,2,(N,N))
            print("The graph :",graph)
            self.N = len(graph)

            source_x = ny.random.randint(0,N)
            print("random source x",source_x)
        
            source_y = ny.random.randint(0,N)
            print("random source y",source_y)
            # source_x = 0
            # source_y = 2

            if graph[source_x][source_y] == 0:
                print("source is invalided")
                #return 0
                print("Again new Grid generate")
                continue
           
            
            goal_x = ny.random.randint(0,N)
            print("random goal x",goal_x)
            goal_y = ny.random.randint(0,N)
            print("random goal y",goal_y)

            if graph[goal_x][goal_y] == 0:
                print("goal is invalided")
                print("Again new Grid generate")
                print()
                continue
                
                #return 0
            # goal_x = 4
            # goal_y = 4
            
            self.source = Node(source_x, source_y, 0)
            self.goal = Node(goal_x, goal_y, self.goal_level)
            self.st_dfs(graph, self.source)

            if self.found:
                print("Goal found")
                print("Number of moves required =", self.goal.depth)
                return 0
            else:
                print("Goal cannot be reached from the starting block")

    def print_direction(self, m, x, y):
        if m == 0:
            print("Moving Down ({}, {})".format(x, y))
        elif m == 1:
            print("Moving Up ({}, {})".format(x, y))
        elif m == 2:
            print("Moving Right ({}, {})".format(x, y))
        else:
            print("Moving Left ({}, {})".format(x, y))

    def st_dfs(self, graph, u):
        graph[u.x][u.y] = 0
        for j in range(self.directions):
            v_x = u.x + self.x_move[j]
            v_y = u.y + self.y_move[j]

            if (0 <= v_x < self.N) and (0 <= v_y < self.N) and graph[v_x][v_y] == 1:
                v_depth = u.depth + 1
                self.print_direction(j, v_x, v_y)

                if v_x == self.goal.x and v_y == self.goal.y:
                    self.found = True
                    self.goal.depth = v_depth
                    return

                child = Node(v_x, v_y, v_depth)
                self.st_dfs(graph, child)

                if self.found:
                    return

def main():
    d = DFS()
    d.init()

if __name__ == "__main__":
    main()
