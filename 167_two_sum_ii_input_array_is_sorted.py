class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        d={}
        for i,n in enumerate(numbers):
            if target-n in d:
                return [d[target-n]+1, i+1]
            d[n] = i
 
