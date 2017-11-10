class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t = {}
        for n in nums:
            if t.has_key(n):
                del t[n]
            else:
                t[n] = 1
        
        return t.keys()[0]
