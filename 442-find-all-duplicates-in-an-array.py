class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Key idea: 
        # sort the array first.
        # then if two consecutive numbers are same, 
        # add them to duplicated numbers list.
        nums = sorted(nums)
        dup = []
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                dup.append(nums[i])
        return dup
