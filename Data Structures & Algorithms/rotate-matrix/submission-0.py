class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        import copy 
        mat1=copy.deepcopy(matrix)
        ROWS=len(matrix)
        COLS=len(matrix[0])
        for i in range(ROWS): # step1= transpose 
            for j in range(COLS):
                matrix[i][j]=mat1[j][i]
        # reverese rows in place 2 pointer technique
        for i in range(ROWS):
            l=0 
            r=COLS-1
            while l<r:
                matrix[i][l],matrix[i][r]=matrix[i][r],matrix[i][l]
                l+=1
                r-=1
        

        


        
        