class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans =[]
        for i in range(len(nums)):
            product=1
            for j in range(len(nums)):
                if i==j:
                    continue 
                else : 
                    product*=nums[j]
            ans.append(product)
        return ans 






























        
        # product=1
        # zerofound = False 
        # for n in nums:
        #     if(n==0):
        #         zerofound = True 
        #         continue 
        #     product*=n
        # for i in range(len(nums)) :
        #     if(zerofound==False):
        #         newval=product//nums[i]
        #         nums[i]=newval
        #     if(zerofound):
        #         if(nums[i]==0):
        #             newval=product
        #             nums[i]=(newval)
        #         else:
        #             nums[i]=0
        # return nums 
        