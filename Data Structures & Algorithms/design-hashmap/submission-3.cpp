class MyHashMap 
{
 vector<pair<int,int>> bucket;
public:
    MyHashMap() 
    {
        bucket.resize(10007,{-1,-1});
    }
     bool contains(int key)
    {
        int index =key%10007;
        if(bucket[index].first==key) return true; 
        return false;
    }
    void put(int key, int value) 
    {
        int index = key%10007;
        if(contains(key))
        {
            bucket[index].second=value;
        }
        else 
        {
            bucket[index].first=key;
            bucket[index].second=value;
        }
    }
    
    int get(int key) 
    {
        int index = key%10007;
        if(contains(key))
        {
            return bucket[index].second;
        }
        return -1;
    }
    
    void remove(int key) 
    { 
        int index = key%10007;
        if(contains(key))
        {
            bucket[index]={-1,-1};
        }
    }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */