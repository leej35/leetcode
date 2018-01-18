class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        """
        # WAY1 : O(N^2)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if target - nums[i] == nums[j]:
                    return [i,j]
        """
        
        #WAY2 : O(N) with hashmap
        hash={}        
        for i,n in enumerate(nums):
            if hash.has_key(n):
                if i != hash[n]:
                    return [hash[n], i]
            else:
                hash[target - n] = i
                
        return False
