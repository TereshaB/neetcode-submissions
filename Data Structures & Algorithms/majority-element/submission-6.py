class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # boyer moore : 
        candidate=nums[0]
        count = 1 
        for i in range(1,len(nums)):
            if(nums[i]==candidate):
                count+=1
            elif(count>0):
                count-=1
            else : 
                candidate=nums[i]
                count=1
        return candidate

# brute force 
    # tracker={}
    # for i in nums:
    #     tracker[i]=tracker.get(i,0)+1
    # pairs = list(tracker.items())
    # pairs.sort(key=lambda x:x[1])
    # result=[]
    # for i in range (k) :
    #     list.append(pairs[-(i+1)[0]])
    # print(list)
#  Boyer moore allows us to save on space complexity wuth O(1) space instead of using any more memory