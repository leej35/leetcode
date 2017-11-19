class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1: return 0
        
        d={}
        
        # get each number's occurrences in d
        for n in nums:
            if not d.has_key(n):
                d[n]=0
            d[n]+=1
        
        # get adjacent numbers joint occurrences in d2
        d2=[]
        _nums = sorted(list(set(nums)))
        for i in range(len(_nums)):
            if i < 1: continue
            if _nums[i] - _nums[i-1] == 1:
                d2.append((_nums[i-1],_nums[i], d[_nums[i-1]]+d[_nums[i]] ))

        if len(d2) < 1: return 0
        
        # get the top frequent adjacent numbers
        n1, n2, _ = sorted(d2, key=lambda x:x[2], reverse=True)[0]
        
        #filter only n1 and n2 from nums
        subseq=[]
        for n in nums:
            if n == n1 or n == n2:
                subseq.append(n)
                
        return len(subseq)
