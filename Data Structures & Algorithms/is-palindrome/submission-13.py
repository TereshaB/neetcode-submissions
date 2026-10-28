class Solution:
    def isPalindrome(self, s: str) -> bool:
        str=""
        for c in s:
            if c.isalnum():
                str+=c
        L,R=0,len(str)-1
        while L<R:
            if str[L].lower()!=str[R].lower():
                return False
            L+=1
            R-=1
        return True