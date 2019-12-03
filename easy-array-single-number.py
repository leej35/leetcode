# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for n in nums:
            if d.has_key(n):
                del d[n]
            else:
                d[n] = 1
                
        return d.keys()[0]
        
# TC : O(n)        
# SC : O(n)
