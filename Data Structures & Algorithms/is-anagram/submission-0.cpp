#include<cstring>
using namespace std;
class Solution {
public:
    bool isAnagram(string s, string t) 
    {
        if(s.length()==t.length())
        {
            sort(s.begin(),s.end());
            sort(t.begin(),t.end());
            int result = strcmp(s.c_str(),t.c_str());
            if(result==0)
            {
                return true;
            }
        }
        return false;
    }
};
