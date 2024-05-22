grid = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
n = len(grid)
ans = ""

def is_valid(r, c):
    return 0 <= r < n and 0 <= c < n and grid[r][c] == 1

def path(cur_r, cur_c, seq):
    global ans  # Use global keyword to modify the global variable 'ans'
    if cur_r == n - 1 and cur_c == n - 1:
        ans = seq
        return True
    
    # Possible moves: down and right
    moves = [[cur_r + 1, cur_c], [cur_r, cur_c + 1]]
    
    for move in moves:
        new_r, new_c = move
        if is_valid(new_r, new_c):
            grid[new_r][new_c] = 2  # Mark as visited
            
            if move == [cur_r + 1, cur_c]:
                new_seq = seq + "D"
            else:
                new_seq = seq + "R"
            
            if path(new_r, new_c, new_seq):
                return True
            
            # Backtracking
            grid[new_r][new_c] = 1
    
    return False

# Initial call to find the path
if path(0, 0, ""):
    print(ans)
else:
    print("No path found")

