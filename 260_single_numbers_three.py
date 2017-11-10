class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        t = {}
        for n in nums:
            if t.has_key(n):
                t[n] += 1
                if t[n] == 2:
                    del t[n]
            else:
                t[n] = 1
        return t.keys()[:2]
