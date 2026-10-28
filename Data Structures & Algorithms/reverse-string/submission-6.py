class Solution:
    def reverseString(self, s: List[str]) -> None:
        left=0
        right=len(s)-1
        def reverse(l,r):
            if(l>=r):
                return 
            s[l],s[r]=s[r],s[l]
            return reverse(l+1,r-1)
        reverse(left,right)


        """
        Do not return anything, modify s in-place instead.
        """
        