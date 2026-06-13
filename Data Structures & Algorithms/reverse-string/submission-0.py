class Solution:
    def reverseString(self, s: List[str]) -> None:
       i=0
       j=len(s)-1
       for t in range(len(s)//2) : 
        temp = s[t]
        s[t]=s[j]
        s[j]=temp
        i+=1
        j-=1
    
        
        