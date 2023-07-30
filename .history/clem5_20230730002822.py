
class Solution:

    def removeIslands(self, matrix):
        self.matrix= matrix
        self.row_length= len(self.matrix)
        self.col_length = len (self.matrix[0])
        self.borderLand()
        for i in range(self.row_length -1):
            for j in range(self.col_length -1):
                if self.matrix[i][j]==1:
                    self.matrix[i][j]=0
                elif self.matrix[i][j]==2:
                    self.matrix[i][j]=1
        return self.matrix
        
    def borderLand(self):
        for i in range(self.row_length -1):
            for j in range (self.col_length -1):
                if self.matrix[i][j]==1:
                    if i == 0 or j==0 or i==self.row_length-1 or j== self.col_length -1:
                        self.markBorderLand(i,j)
    
    def markBorderLand(self, i, j):
        if i < 0 or j <0 or i==self.row_length or j==col_length:
            return
        self.matrix[i][j]=2
        markBorderLand(i+1, j)
        markBorderLand(i-1, j)
        markBorderLand(i, j-1)
        markBorderLand(i, j+1)