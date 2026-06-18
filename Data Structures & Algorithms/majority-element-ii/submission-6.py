# Optimized soln O(1)space
            
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = defaultdict(int)
        for n in nums : 
            counter[n]+=1
            if(len(counter)<3):
                continue
            res=defaultdict(int)
            for n,c in counter.items():
                counter[n]-=1
                if(c>0):
                    res[n]=c
            counter=res
        ans=[]
        for n in counter : 
            if nums.count(n)> len(nums)//3:
                ans.append(n)
        return ans 
