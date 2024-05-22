grid = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
n = len(grid)

def is_valid(r, c):
    return 0 <= r < n and 0 <= c < n and grid[r][c] == 1

def find_path(cur_r, cur_c, path):
    if cur_r == n - 1 and cur_c == n - 1:
        return True, path
    
    # Possible moves: down and right
    moves = [[cur_r + 1, cur_c], [cur_r, cur_c + 1]]
    
    for move in moves:
        new_r, new_c = move
        if is_valid(new_r, new_c):
            # Mark as visited
            grid[new_r][new_c] = 2  # Use 2 to mark visited cells
            
            if move == [cur_r + 1, cur_c]:
                new_path = path + "D"
            else:
                new_path = path + "R"
            
            found, result_path = find_path(new_r, new_c, new_path)
            if found:
                return True, result_path
            
            # Backtracking
            grid[new_r][new_c] = 1
    
    return False, path

# Initial call to find the path
found, result_path = find_path(0, 0, "")
if found:
    print(result_path)
else:
    print("No path found")
print(grid)    
