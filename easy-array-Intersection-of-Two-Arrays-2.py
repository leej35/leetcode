# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        # change to dict
        def to_dict(alist):
            d = {}
            for a in alist:
                if a in d:
                    d[a] += 1
                else:
                    d[a] = 1
            return d
        # n: len(nums1), m: len(nums2)
        # O(n) + O(m)
        d1 = to_dict(nums1)
        d2 = to_dict(nums2)
        
        # determine longer and shorter one
        if len(d1) > len(d2):
            longer, shorter = d1, d2
        else:
            longer, shorter = d2, d1
        
        # find match with loop over shorter one.
        # inside loop, use hash in O(1)
        # in total => O(n)
        match = []
        for k in shorter.keys():
            if k in longer:
                nrepeat = min(shorter[k], longer[k])
                match += [k] * nrepeat
                
        return match
    
