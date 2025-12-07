class GraphColoringBacktracking:
    def __init__(self, graph, num_colors):
        self.graph = graph  # The graph as an adjacency matrix or adjacency list
        self.num_colors = num_colors  # Number of available colors
        self.num_vertices = len(graph)
        self.colors = [-1] * self.num_vertices  # Initially, no color is assigned

    # Function to check if it is safe to color vertex with a given color
    def is_safe(self, vertex, color):
        for i in range(self.num_vertices):
            if self.graph[vertex][i] == 1 and self.colors[i] == color:
                return False
        return True

    # Function to solve the graph coloring problem using backtracking
    def solve(self, vertex):
        if vertex == self.num_vertices:
            self.print_solution()
            return True

        for color in range(self.num_colors):
            if self.is_safe(vertex, color):
                self.colors[vertex] = color
                if self.solve(vertex + 1):  # Try coloring the next vertex
                    return True
                self.colors[vertex] = -1  # Backtrack

        return False

    # Function to print the solution
    def print_solution(self):
        print("Solution:")
        for i in range(self.num_vertices):
            print(f"Vertex {i} -> Color {self.colors[i]}")
        print()

# Example usage:
graph = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
]

num_colors = 3
graph_coloring = GraphColoringBacktracking(graph, num_colors)
if not graph_coloring.solve(0):
    print("Solution does not exist")