from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nc = {k:v for k,v in Counter(nums).iteritems()}
        nc = sorted(nc.items(), key=lambda x:x[1], reverse=True)
        return nc[0][0]
        
        
