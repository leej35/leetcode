class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        h = {}
        
        # 1. count frequency
        for n in nums:
            if h.has_key(n):
                h[n] += 1
            else:
                h[n] = 1
        
        # 2. sort
        l = [(f,n) for n,f in h.iteritems()]
        l = sorted(l, key=lambda x:x[0], reverse=True)
        
        # 3. get result
        return [n for f,n in l[:k]]
        
