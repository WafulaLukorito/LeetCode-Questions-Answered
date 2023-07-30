

def removeIslands(matrix):
    row_length = len(matrix)
    col_length = len(matrix[0])
    
    #Mark all lands connected to the border as 2
    def dfs(i, j):
        if i<0 or j< 0 or i == row_length or j == col_length or matrix[i][j] !=1:
            return
        matrix[i][j]=2
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
    
    #Mark all lands connected to the border
    for i in range(row_length):
        for j in range(col_length):
            is_border = i == 0 or j == 0 or i == row_length -1 or j== col_length-1
            if is_border and matrix[i][j] ==1:
                dfs(i, j)
                
 # All lands marked as 2 are the lands connected to the border, keep them as 1
    # All lands marked as 1 are islands, remove them by marking as 0
    
    for i in range(row_length):
        for j in range(col_length):
            if matrix[i][j]==1:
                matrix[i][j]=0
            elif matrix[i][j]==2:
                matrix[i][j]=1

    return matrix