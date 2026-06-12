
class Solution {
public:
    int majorityElement(vector<int>& nums) 
    { int max=0;
    int ans ;
        unordered_map<int,int> track;
        for(int i : nums)
        {
            track[i]++;
        }
        for(auto&[key,value]:track)
        {
            if(value>max)
            {
                max =value;
                ans = key;
            }
        }
        return ans;
    }
};
    