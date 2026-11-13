class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        l,r=0,len(matrix[0]) # col
        t,b=0,len(matrix) # row
        while l<r and t<b:
            # top row
            for i in range(l,r):
                res.append(matrix[t][i])
            t+=1
            # right col
            for i in range(t,b):
                res.append(matrix[i][r-1]) # right is set to be out of bounds to r-1
            r-=1
            if not (l<r and t<b): # 1 rowed/columned matrix case
                break
            # bottom row
            for i in range(r-1,l-1,-1):
                res.append(matrix[b-1][i])
            b-=1
            # left col
            for i in range (b-1,t-1,-1):
                res.append(matrix[i][l])
            l+=1
        return res