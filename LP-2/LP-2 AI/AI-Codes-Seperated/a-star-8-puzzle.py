import heapq

# Goal state
goal = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]

# Get position of value in the goal state
def goal_position(val):
    for i in range(3):
        for j in range(3):
            if goal[i][j] == val:
                return (i, j)

# Heuristic: Manhattan Distance
def manhattan(state):
    dist = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                gi, gj = goal_position(val)
                dist += abs(i - gi) + abs(j - gj)
    return dist

# Find (i, j) of blank (0)
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return (i, j)

# Generate next possible states
def get_neighbors(state):
    x, y = find_blank(state)
    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    neighbors = []
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

# Convert board to a tuple for hashing
def to_tuple(board):
    return tuple(tuple(row) for row in board)

# Print board
def print_board(board):
    for row in board:
        print(row)
    print()

# A* algorithm
def solve(start):
    open_list = []
    heapq.heappush(open_list, (manhattan(start), 0, start, []))
    visited = set()

    while open_list:
        f, g, current, path = heapq.heappop(open_list)
        visited.add(to_tuple(current))

        if current == goal:
            for step in path + [current]:
                print_board(step)
            return

        for neighbor in get_neighbors(current):
            if to_tuple(neighbor) not in visited:
                new_path = path + [current]
                heapq.heappush(open_list, (g + 1 + manhattan(neighbor), g + 1, neighbor, new_path))

# Example start state
start = [[1, 2, 3],
         [4, 0, 6],
         [7, 5, 8]]

solve(start)
