class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = 0
        nums = sorted(nums, reverse=True)
        for i, n in enumerate(list(nums)):
            if i % 2 == 1:
                r += n
        return r
