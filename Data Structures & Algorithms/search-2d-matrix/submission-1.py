class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS=len(matrix)
        COLS=len(matrix[0])
        top=0
        bot=ROWS-1
        while top<=bot:
            row=(top+bot)//2
            if target>matrix[row][-1]:
                top=row+1
            elif target<matrix[row][0]:
                bot=row-1
            else:
                break
        if not (top<=bot):
            return False
        row =(top+bot)//2
        L=0
        R=COLS-1
        while L<=R:
            m=(L+R)//2
            if target<matrix[row][m]:
                R=m-1
            elif target>matrix[row][m]:
                L=m+1
            else :
                return True
        return False

  
        