import heapq

def dijkstra(graph, start):
    # Step 1: Initialize distances and previous nodes
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous = {node: None for node in graph}

    # Step 2: Min-heap for the next closest node
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # Step 3: Skip if we've already found a shorter path
        if current_distance > distances[current_node]:
            continue

        # Step 4: Check all neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # Step 5: Update distance if a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    return distances, previous

# Function to get the full path from start to a node
def get_path(previous, node):
    path = []
    while node:
        path.insert(0, node)
        node = previous[node]
    return path

# Define the graph
graph = {
    'A': [('B', 4), ('C', 5)],
    'B': [('A', 4), ('C', 11), ('D', 9), ('E', 7)],
    'C': [('A', 5), ('B', 11), ('E', 3)],
    'D': [('B', 9), ('F', 2)],
    'E': [('B', 7), ('C', 3), ('F', 6)],
    'F': [('D', 2), ('E', 6)]
}

# Run Dijkstra from node 'A'
distances, previous = dijkstra(graph, 'A')

# Print the results
print("Shortest distances and paths from A:")
for node in sorted(graph.keys()):
    path = get_path(previous, node)
    print(f"{node}: Distance = {distances[node]}, Path = {' -> '.join(path)}")
