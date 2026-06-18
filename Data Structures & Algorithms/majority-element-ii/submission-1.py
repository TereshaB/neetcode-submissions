class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter ={}
        ans=[]
        size =len(nums)
        counter= defaultdict(int) # avoids key error 
        for i in nums :
            counter[i]+=1
        for key,value in counter.items():
            if(value>(size//3)):
                ans.append(key)
        return ans
            
# brute force O(n) time and O(n) space 
        
