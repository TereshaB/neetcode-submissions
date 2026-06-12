
/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */
 class MyHashSet {
public:
vector<vector<int>> buckets;
    MyHashSet() 
    {
            buckets.resize(10007);
    }
    
    void add(int key) 
    {
     if(!contains(key))
       { int index = key %10007;
        buckets[index].push_back(key);
       }
    }
    
    void remove(int key)
    {
    if(contains(key))
    {
        int index=key%10007;

    buckets[index].erase(std::remove(buckets[index].begin(),buckets[index].end(),key),buckets[index].end());
    }
    }
    
    bool contains(int key) 
    {
        int index = key%10007;
        for(int x:buckets[index])
        {
            if (x==key) return true;
        }
        return false;
    }
};