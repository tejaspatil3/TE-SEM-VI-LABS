import heapq

# Define the possible movements (left, right, up, down)
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def heuristic(a, b):
    """Manhattan distance heuristic"""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, goal):
    """
    A* algorithm to find the shortest path in a grid.
    :param grid: 2D list representing the grid (0 is free space, 1 is obstacle)
    :param start: tuple (x, y) representing the start position
    :param goal: tuple (x, y) representing the goal position
    :return: List of tuples representing the path from start to goal (empty list if no path)
    """
    # Get grid dimensions
    rows, cols = len(grid), len(grid[0])

    # Open list (priority queue) to store nodes to be evaluated
    open_list = []
    heapq.heappush(open_list, (0 + heuristic(start, goal), 0, start))  # (f_score, g_score, node)
    
    # Closed list to store nodes that have already been evaluated
    closed_list = set()
    
    # Dictionary to store the parent of each node to reconstruct the path
    came_from = {}

    # g_score dictionary to store the cost of the path from the start to each node
    g_score = {start: 0}
    
    while open_list:
        # Get the node with the lowest f_score
        _, current_g_score, current = heapq.heappop(open_list)
        
        # If the current node is the goal, reconstruct the path
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # Reverse the path to go from start to goal
        
        # Add current node to closed list
        closed_list.add(current)
        
        # Explore neighbors
        for dx, dy in MOVES:
            neighbor = (current[0] + dx, current[1] + dy)
            
            # Skip if the neighbor is out of bounds or an obstacle
            if not (0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols) or grid[neighbor[0]][neighbor[1]] == 1:
                continue
            
            # Skip if the neighbor is in the closed list
            if neighbor in closed_list:
                continue
            
            # Calculate the tentative g_score for the neighbor
            tentative_g_score = current_g_score + 1
            
            # If the neighbor is not in the open list, add it
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_score, tentative_g_score, neighbor))
    
    # Return an empty list if no path is found
    return []

def print_grid_with_path(grid, path):
    """Print the grid with the path marked"""
    grid_copy = [row[:] for row in grid]  # Make a copy of the grid
    for (x, y) in path:
        grid_copy[x][y] = '-'  # Mark the path with '2'
    
    # Print the grid with path
    for row in grid_copy:
        print(' '.join(str(cell) for cell in row))

# Example grid (0 = free space, 1 = obstacle)
grid = [
    [0, 0, 0, 1, 1],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

# Define start and goal positions
start = (0, 0)  # Top-left corner
goal = (4, 4)   # Bottom-right corner

# Find the shortest path using A* algorithm
path = a_star(grid, start, goal)

if path:
    print("Path found:")
    print_grid_with_path(grid, path)
else:
    print("No path found.")
