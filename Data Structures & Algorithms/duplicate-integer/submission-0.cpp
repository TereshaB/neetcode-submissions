class Solution {
public:
    bool hasDuplicate(vector<int>& nums) 
    {
        sort(nums.begin(),nums.end());
        int i =0 ,j=1;
        if(nums.size()>1)
        {
            for(  i ;i<(nums.size()-1);i++)
            {

                if(nums[i]==nums[j])
                {
                    return true;
                }
                else j++;
            }
        }
    return false;
    }
};