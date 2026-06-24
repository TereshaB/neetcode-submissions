class NumArray:

    def __init__(self, nums: List[int]):
      prefix=0
      self.ans =[0]*len(nums)
      for i in range(len(nums)): 
         prefix+=nums[i]
         self.ans[i]=prefix
    def sumRange(self, left: int, right: int) -> int:
        sum=0
        if(left==0):
            sum=self.ans[right]
        else :
            sum=(self.ans[right])-(self.ans[left-1])
        return sum

        

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)