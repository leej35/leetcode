class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        maxlen = 0
        while nums:
            
            first = last = nums.pop()
            
            while first - 1 in nums:
                first -= 1
                nums.remove(first)
            
            while last +1 in nums:
                last += 1
                nums.remove(last)
            
            maxlen = max(maxlen, last - first +1)
        
        return maxlen
                
