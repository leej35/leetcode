class Solution(object):
    def canPlaceFlowers(self, f, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        def is_adjacent_empty(i,f):
            right,left = True,True
            if i-1 > -1 and f[i-1] == 1:
                left = False
            if i+1 < len(f) and f[i+1] == 1:
                right = False
            return left and right
        
        for i in range(len(f)):
            if is_adjacent_empty(i,f) and f[i] == 0 and n > 0 :
                f[i] = 1
                n-=1
        
        return n == 0
