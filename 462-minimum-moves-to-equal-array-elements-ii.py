# key idea: get median and sum differences of each number and the median.

class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        median = sorted(nums)[len(nums)/2]
        return sum([abs(median-n) for n in nums])a
