import heapq

def greedy_sssp(graph, start):
    # Step 1: Initialization
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    min_heap = [(0, start)]  # (distance, node)
    
    while min_heap:
        current_distance, current_node = heapq.heappop(min_heap)
        
        # If the distance in the heap is greater than the recorded distance, skip
        if current_distance > distances[current_node]:
            continue
        
        # Step 2: Explore neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))
    
    return distances

# Example graph (adjacency list)
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

# Run greedy SSSP from node 'A'
shortest_distances = greedy_sssp(graph, 'A')
print("Shortest distances from source A:")
for node, distance in shortest_distances.items():
    print(f"A -> {node} = {distance}")


#  Dry Run Table (Start from A)
# Step	Node Chosen	Distance from A	Distance Updates
# 1	A	0	B=1, C=4
# 2	B	1	C=3 (better), D=6
# 3	C	3	D=4 (better)
# 4	D	4	—

# Final distances:

# A → A = 0

# A → B = 1

# A → C = 3

# A → D = 4

# 📌 Key Properties
# Greedy Choice: Always expand the node with the smallest known distance.

# Data Structure: Min-Heap (heapq) ensures that the node with the smallest distance is efficiently selected at each step.

# Time Complexity:

# Using Min-Heap: O((V + E) log V) where V is the number of vertices and E is the number of edges.

# This algorithm works effectively when all edge weights are non-negative, and is optimal for the single source shortest path problem.

# The Single Source Shortest Path (SSSP) problem aims to find the shortest paths from a single source vertex to all other vertices in a graph. The Greedy Search approach can be applied here using Dijkstra's Algorithm, which is a well-known algorithm for solving the SSSP problem with non-negative edge weights.

# The greedy strategy is to always choose the node with the smallest tentative distance and explore its neighbors. This leads to an optimal solution for the shortest paths in graphs with non-negative weig

#  Steps for the Greedy Search Algorithm (Dijkstra’s Algorithm):
# Initialization:

# Set the initial distance to 0 for the source node and ∞ for all other nodes.

# Use a priority queue (min-heap) to keep track of the node with the smallest distance.

# Relaxation:

# Extract the node with the smallest distance.

# For each of its neighbors, update their distances if a shorter path is found.

# Repeat until all nodes are processed.