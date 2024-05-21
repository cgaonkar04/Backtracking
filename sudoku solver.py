grid = [
    [3, 8, 5, 0, 0, 0, 0, 0, 0],
    [9, 2, 1, 0, 0, 0, 0, 0, 0],
    [6, 4, 7, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 2, 3, 0, 0, 0],
    [0, 0, 0, 7, 8, 4, 0, 0, 0],
    [0, 0, 0, 6, 9, 5, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 8, 7, 3],
    [0, 0, 0, 0, 0, 0, 9, 6, 2],
    [0, 0, 0, 0, 0, 0, 1, 4, 5]
]


def row_taken(row):
    row_taken=[]
    for i in range(9):
        if grid[row][i]!=0:
            row_taken.append(grid[row][i])
    return row_taken    

def col_taken(col):
    col_taken=[]
    for i in range(9):
        if grid[i][col]!=0:
            col_taken.append(grid[i][col])
    return col_taken 

def mini_grid_taken(row,col):
    mini_grid_taken=[]
    r=row%3
    c=col%3
    for i in range(row-r,row-r+3):
        for j in range(col-c,col-c+3):
            if grid[i][j]!=0:
                mini_grid_taken.append(grid[i][j])
    return mini_grid_taken 

def solver(grid,row,col):
    if row==9:
        return True
    elif col==9:
        return solver(grid,row+1,0)
    elif grid[row][col]!=0:
        return solver(grid,row,col+1)
    else:
        for k in range(1,10):
            if k not in row_taken(row) and k not in col_taken(col) and k not in mini_grid_taken(row,col):
                grid[row][col]=k
                if solver(grid,row,col+1):
                    return True
                grid[row][col]=0
        return False

print(solver(grid,0,0))
print(grid)            
    
