class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs)
    {
        vector<vector <string>> ans;
        unordered_map<string,vector<string>> store;
        for(string s: strs)
        {
            string key =s;
            sort(key.begin(),key.end());
            store[key].push_back(s);
        }
        for(auto &[key,value]: store)
        {
            ans.push_back(value);
        }
        return ans;
    }
};
