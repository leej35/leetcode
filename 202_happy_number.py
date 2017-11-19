class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def sqsum(num):
            v=0
            for n in list(str(num)):
                v+=int(n)**2
            return v
        
        hist=[]
        
        while True:
            n = sqsum(n)
            if n in hist:
                return False
            if sqsum(n) == 1:
                return True
            hist.append(n)
            
            
