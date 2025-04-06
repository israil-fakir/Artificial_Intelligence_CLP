def is_safe(node, color, assignment, graph):
    for neighbor in graph[node]:
        if assignment[neighbor] == color:
            return False
    return True

def graph_coloring(node, assignment, graph, K, N):
    if node == N:
        return True

    for color in range(1, K + 1):
        if is_safe(node, color, assignment, graph):
            assignment[node] = color
            if graph_coloring(node + 1, assignment, graph, K, N):
                return True
            assignment[node] = 0  # Backtrack
    return False

def solve_graph_coloring():
    # Read input values separately
    N = int(input("Enter number of vertices (N): "))
    M = int(input("Enter number of edges (M): "))
    K = int(input("Enter number of colors (K): "))

    # Build the graph
    graph = [[] for _ in range(N)]
    print(f"Enter {M} edges (u v):")
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    assignment = [0] * N
    if graph_coloring(0, assignment, graph, K, N):
        print(f"\nColoring Possible with {K} Colors")
        print("Color Assignment:", assignment)
    else:
        print(f"\nColoring Not Possible with {K} Colors")

# Run the function
if __name__ == "__main__":
    solve_graph_coloring()
