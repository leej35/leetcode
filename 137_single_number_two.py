class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t={}
        for n in nums:
            if t.has_key(n):
                t[n]+=1
                if t[n] == 3:
                    del t[n]
            else:
                t[n]=1
        return t.keys()[0]
