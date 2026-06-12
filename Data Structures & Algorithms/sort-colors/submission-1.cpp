class Solution {
public:
    void sortColors(vector<int>& nums) 
    {
        map<int,int> m;
        m[0]=0;
        m[1]=0;
        m[2]=0;
        for(int val:nums)
        {
            m[val]++;
        }
        nums.clear();

        for(auto &[key,value]:m)
        {
            int count =value;
            for(int i =0;i<count;i++)
            {
                nums.push_back(key);
            }
        }
    }
};