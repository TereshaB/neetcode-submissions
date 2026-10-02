class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.rstrip(" ")
        lword=[]
        for i in range((len(s)-1),-1,-1):
            if(s[i]==" "):
                break
            else:
                lword.append(s[i])
        ans=len(lword)
        return ans 
        