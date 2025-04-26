import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cluster = None

class KMeans:
    def __init__(self, num_points=100, num_clusters=10):
        self.num_points = num_points
        self.num_clusters = num_clusters
        self.grid_size = 25
        self.points = [Point(random.randint(0, self.grid_size-1), random.randint(0, self.grid_size-1)) for _ in range(num_points)]
        self.centroids = [Point(random.randint(0, self.grid_size-1), random.randint(0, self.grid_size-1)) for _ in range(num_clusters)]

    def manhattan_distance(self, p1, p2):
        return abs(p1.x - p2.x) + abs(p1.y - p2.y)

    def assign_clusters(self):
        for point in self.points:
            distances = [self.manhattan_distance(point, centroid) for centroid in self.centroids]
            point.cluster = distances.index(min(distances))

    def update_centroids(self):
        changed = False
        for i in range(self.num_clusters):
            cluster_points = [p for p in self.points if p.cluster == i]
            if cluster_points:
                avg_x = sum(p.x for p in cluster_points) // len(cluster_points)
                avg_y = sum(p.y for p in cluster_points) // len(cluster_points)
                if self.centroids[i].x != avg_x or self.centroids[i].y != avg_y:
                    self.centroids[i].x = avg_x
                    self.centroids[i].y = avg_y
                    changed = True
            else:
                self.centroids[i] = Point(random.randint(0, self.grid_size-1), random.randint(0, self.grid_size-1))
                changed = True
        return changed

    def fit(self):
        while True:
            self.assign_clusters()
            if not self.update_centroids():
                break

    def visualize(self):
        matrix = [['.' for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        for c in self.centroids:
            matrix[c.y][c.x] = 'C'
        for p in self.points:
            if matrix[p.y][p.x] == '.':
                matrix[p.y][p.x] = str(p.cluster % 10)
        for row in reversed(matrix):
            print(' '.join(row))

# Run the algorithm
kmeans = KMeans()
kmeans.fit()
kmeans.visualize()