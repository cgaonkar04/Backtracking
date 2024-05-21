# Initialize an 8x8 grid
grid = [[0 for _ in range(8)] for _ in range(8)]
start_row, start_col = 0, 0  # Starting position

# Function to get possible moves for a knight from the current position
def get_moves(row, col):
    moves = [[-2, 1], [-2, -1], [2, 1], [2, -1], [-1, 2], [-1, -2], [1, 2], [1, -2]]
    valid_moves = []
    for move in moves:
        new_row, new_col = row + move[0], col + move[1]
        if 0 <= new_row < 8 and 0 <= new_col < 8 and grid[new_row][new_col] == 0:
            valid_moves.append((new_row, new_col))
    return valid_moves

# Function to apply Warnsdorff's rule
def sorted_moves(row, col):
    possible_moves = get_moves(row, col)
    # Sort the possible moves by the number of further moves they have (fewest first)
    return sorted(possible_moves, key=lambda move: len(get_moves(move[0], move[1])))

# Solver function using backtracking and Warnsdorff's rule
def solver(row, col, counter):
    if counter == 64:
        return True
    else:
        for move in sorted_moves(row, col):
            new_row, new_col = move
            grid[new_row][new_col] = counter + 1
            if solver(new_row, new_col, counter + 1):
                return True
            grid[new_row][new_col] = 0
        return False

# Starting the tour
grid[start_row][start_col] = 1
if solver(start_row, start_col, 1):
    for row in grid:
        print(row)
else:
    print("No solution found")
