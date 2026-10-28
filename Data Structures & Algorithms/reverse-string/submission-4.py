class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        st=[]
        for c in s :
            st.append(c)
        st_len=len(st)-1
        for i in range (len(s)):
            s[i]=st[st_len]
            st_len-=1
    #    O(n)-> time 
    #    O(n)-> space
    #    Method 2 : using stack

