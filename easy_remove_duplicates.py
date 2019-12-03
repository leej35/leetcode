# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ptr_0 = 1  # pointer to current element
        
        while(ptr_0 < len(nums)):
            if nums[ptr_0 - 1] == nums[ptr_0]:
                del nums[ptr_0 - 1]
            else:
                ptr_0 += 1
        
        return len(nums)
            
            
