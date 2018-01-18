# Key idea: a result number = (multiple on left-side) * (right-side)

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        left, right, ans = [1]*(n+1), [1]*(n+1), [1]*n
        
        for i in range(1,n):
            left[i] = left[i-1] * nums[i-1]
        
        for j in range(n,1,-1):
            right[j-1] = right[j] * nums[j-1]
        
        for i in range(n):
            ans[i] = left[i]*right[i+1]
            
        return ans
        
