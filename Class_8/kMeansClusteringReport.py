import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cluster = None

class KMeansManhattan:
    def __init__(self, num_points=100, num_clusters=10, grid_size=20):
        self.num_points = num_points
        self.num_clusters = num_clusters
        self.grid_size = grid_size
        self.points = [Point(random.randint(0, grid_size-1), random.randint(0, grid_size-1)) for _ in range(num_points)]
        self.centroids = [Point(random.randint(0, grid_size-1), random.randint(0, grid_size-1)) for _ in range(num_clusters)]

    def manhattan_distance(self, p1, p2):
        return abs(p1.x - p2.x) + abs(p1.y - p2.y)

    def assign_clusters(self):
        for point in self.points:
            min_dist = float('inf')
            for i, centroid in enumerate(self.centroids):
                dist = self.manhattan_distance(point, centroid)
                if dist < min_dist:
                    min_dist = dist
                    point.cluster = i

    def update_centroids(self):
        new_centroids = []
        for i in range(self.num_clusters):
            cluster_points = [p for p in self.points if p.cluster == i]
            if cluster_points:
                avg_x = sum(p.x for p in cluster_points) // len(cluster_points)
                avg_y = sum(p.y for p in cluster_points) // len(cluster_points)
                new_centroids.append(Point(avg_x, avg_y))
            else:
                new_centroids.append(Point(random.randint(0, self.grid_size-1), random.randint(0, self.grid_size-1)))
        changed = any(c.x != nc.x or c.y != nc.y for c, nc in zip(self.centroids, new_centroids))
        self.centroids = new_centroids
        return changed

    def fit(self):
        iteration = 0
        while True:
            self.assign_clusters()
            changed = self.update_centroids()
            if not changed:
                break
            iteration += 1

    def visualize(self):
        matrix = [['.' for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        for c in self.centroids:
            matrix[c.y][c.x] = 'C'  # Cluster center
        symbols = ['0','1','2','3','4','5','6','7','8','9']
        for p in self.points:
            if matrix[p.y][p.x] == '.':
                matrix[p.y][p.x] = symbols[p.cluster % 10]
        for row in matrix[::-1]:  # Print from top to bottom
            print(' '.join(row))

# Run the clustering
kmeans = KMeansManhattan()
kmeans.fit()
kmeans.visualize()