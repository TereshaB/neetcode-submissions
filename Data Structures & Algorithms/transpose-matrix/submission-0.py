class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows,columns=len(matrix),len(matrix[0])
        res=[[0]*rows for _ in range(columns)]
        for r in range (rows):
            for c in range (columns):
                res[c][r]=matrix[r][c]
        return res

        