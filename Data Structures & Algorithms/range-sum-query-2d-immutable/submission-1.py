class NumMatrix:

    def __init__(self, matrix: List[List[int]]): 
        row = len(matrix)
        column = len(matrix[0])
        self.newmat= [[0]*(column+1) for _ in range (row+1)]

        for r in range (1,row+1): 
            prefix=0
            for c in range (1,column+1):
                prefix+=matrix[r-1][c-1]
                above=self.newmat[r-1][c]
                self.newmat[r][c]=prefix+above

      
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1,col1,row2,col2=row1+1,col1+1,row2+1,col2+1
        sum=self.newmat[row2][col2]
        above=self.newmat[row1-1][col2]
        left=self.newmat[row2][col1-1]
        topleft=self.newmat[row1-1][col1-1]
        sum=sum-above-left
        sum+=topleft
        return sum



        

     

     
     
            



      


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)