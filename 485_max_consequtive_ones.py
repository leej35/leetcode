class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=[str(n) for n in nums]
        nums=''.join(nums)       
        spl=nums.split('0')
        longseq=sorted(spl, key=lambda x:len(x), reverse=True)[0]
        return len(longseq)
