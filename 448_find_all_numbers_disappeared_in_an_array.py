class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        A = set(range(len(nums)+1)[1:])
        B = set(nums)
        return list(A-B)
