import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cluster = None

class KMeans:
    def __init__(self, points=100, clusters=10):
        self.pt = points
        self.ks = clusters
        self.grid_size = 25
        self.p = [Point(random.randint(0, self.grid_size-1), random.randint(0, self.grid_size-1)) for _ in range(self.pt)]
        self.k = [Point(random.randint(0, self.grid_size-1), random.randint(0, self.grid_size-1)) for _ in range(self.ks)]

    def manhattan_distance(self, p1, p2):
        return abs(p1.x - p2.x) + abs(p1.y - p2.y)

    def assign_clusters(self):
        for point in self.p:
            min_dist = float('inf')
            for j, centroid in enumerate(self.k):
                dist = self.manhattan_distance(point, centroid)
                if dist < min_dist:
                    point.cluster = j
                    min_dist = dist

    def update_centroids(self):
        changed = False
        new_k = []
        for j in range(self.ks):
            cx, cy, count = 0, 0, 0
            for point in self.p:
                if point.cluster == j:
                    cx += point.x
                    cy += point.y
                    count += 1
            if count > 0:
                new_x = cx // count
                new_y = cy // count
            else:
                new_x = random.randint(0, self.grid_size-1)
                new_y = random.randint(0, self.grid_size-1)
            if new_x != self.k[j].x or new_y != self.k[j].y:
                changed = True
            self.k[j].x = new_x
            self.k[j].y = new_y
        return changed

    def fit(self):
        while True:
            self.assign_clusters()
            if not self.update_centroids():
                break

    def visualize(self):
        matrix = [['.' for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        for c in self.k:
            matrix[c.y][c.x] = 'C'
        for point in self.p:
            symbol = str(point.cluster % 10)
            if matrix[point.y][point.x] == '.':
                matrix[point.y][point.x] = symbol
        for row in matrix[::-1]:
            print(' '.join(row))

model = KMeans()
model.fit()
model.visualize()