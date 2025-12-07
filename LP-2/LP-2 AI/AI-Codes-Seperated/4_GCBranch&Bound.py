class GraphColoringBranchAndBound:
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

    # Function to find the next vertex to color (a heuristic to improve the solution)
    def select_uncolored_vertex(self):
        # A simple heuristic: choose the first uncolored vertex
        for vertex in range(self.num_vertices):
            if self.colors[vertex] == -1:
                return vertex
        return -1

    # Function to solve the graph coloring problem using Branch and Bound
    def solve(self, vertex):
        # All vertices are colored, return True
        if vertex == self.num_vertices:
            self.print_solution()
            return True

        # Try coloring the current vertex with available colors
        for color in range(self.num_colors):
            if self.is_safe(vertex, color):
                self.colors[vertex] = color

                # Proceed to color the next vertex
                next_vertex = self.select_uncolored_vertex()
                if next_vertex != -1 and self.solve(next_vertex):
                    return True

                # Backtrack if no solution is found
                self.colors[vertex] = -1

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
graph_coloring = GraphColoringBranchAndBound(graph, num_colors)
if not graph_coloring.solve(0):
    print("Solution does not exist")
