class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        head=0
        for elem in range(len(nums)):
            if nums[elem] != 0:
                if elem != head:
                    nums[head] = nums[elem]
                    nums[elem] = 0
                head+=1
