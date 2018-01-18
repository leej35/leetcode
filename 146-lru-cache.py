class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.map={}
        self.history=[]
        self.capacity = capacity
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.map.has_key(key):
            self.history.remove(key)
            self.history.append(key)
            return self.map[key]
        
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        
        if key not in self.history and len(self.history) >= self.capacity:
            rmkey = self.history[0]
            self.history.remove(rmkey)
            del self.map[rmkey]
        
        if key in self.history:
            self.history.remove(key)
            
        self.history.append(key)
        self.map[key] = value

        
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
