class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        el_n = sum([len(l) for l in nums])
        if r*c != el_n:
            return nums
        
        height = len(nums)
        width = el_n / height
        
        # flatten first
        _nums = []
        for row in nums:
            _nums += row
            
        # reshape
        new = []
        for i in range(r):
            c_st = i*c 
            c_en = (i+1)*c
            new.append(_nums[c_st:c_en])
            
        return new
