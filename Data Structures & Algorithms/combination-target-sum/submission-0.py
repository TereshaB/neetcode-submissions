class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def dfs(i,curr,total):
            if total==target:
                res.append(curr.copy())
                return 
            if total>target or i>=len(nums):
                return 
            # consider the number 
            curr.append(nums[i])
            dfs(i,curr,total+nums[i])
            # don't consider the number
            curr.pop()
            dfs(i+1,curr,total)
        dfs(0,[],0)
        return res

        

# time = O(2^target)
        