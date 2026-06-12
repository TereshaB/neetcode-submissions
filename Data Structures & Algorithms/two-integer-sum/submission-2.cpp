class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) 
    { vector<int> ans;
        unordered_map <int,int> freq;
        for(int i =0 ;i<nums.size();i++)
        {
            int diff = target-nums[i];
            if(freq.count(diff))
            {
                ans.push_back(freq[diff]);
                    ans.push_back(i);
            }
            else
            {
                freq[nums[i]]=i;
            }
        }
        return ans;
    }
};
