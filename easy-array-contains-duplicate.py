# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ## Version : using hash
        # d = {}
        # for n in nums:
        #     if not n in d:
        #         d[n] = 1
        #     else:
        #         return True
        # return False
                
        
        
        ## Version: using sort
        nums = sorted(nums)
        
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                return True
            
        return False
