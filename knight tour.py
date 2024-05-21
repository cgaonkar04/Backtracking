# Initialize an 8x8 grid
grid = [[-1 for _ in range(8)] for _ in range(8)]
start_row, start_col = 0, 0  # Starting position

# Possible moves for a knight
moves = [[-2, 1], [-2, -1], [2, 1], [2, -1], [-1, 2], [-1, -2], [1, 2], [1, -2]]

def is_safe(x, y):
    return 0 <= x < 8 and 0 <= y < 8 and grid[x][y] == -1

# Function to get possible moves for a knight from the current position
def pos(row, col):
    filtered = []
    for move in moves:
        new_row, new_col = row + move[0], col + move[1]
        if is_safe(new_row, new_col):
            filtered.append([new_row, new_col])
    return filtered

# Solver function using backtracking
def solver(row, col, counter):
    if counter == 64:  # All cells are visited
        return True
    for next_move in pos(row, col):
        new_row, new_col = next_move
        grid[new_row][new_col] = counter
        if solver(new_row, new_col, counter + 1):
            return True
        grid[new_row][new_col] = -1  # Backtracking
    return False

# Starting the tour
grid[start_row][start_col] = 0  # Starting position is marked with 0
if solver(start_row, start_col, 1):
    for row in grid:
        print(row)
else:
    print("No solution found")
