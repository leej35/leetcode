class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        ######
        # IMPORTANT KEY IDEA: Square number of (n^2) is sum of first n odd numbers
        # 1 : 1
        # 4 : 1 + 3
        # 9 : 1 + 3 + 5
        ######
        i=n=0
        while True:
            n += 2*i+1
            i+=1
            if num == n : 
                return True
            if num < n:
                return False
        
