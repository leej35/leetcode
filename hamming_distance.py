class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x = bin(x)[2:]
        y = bin(y)[2:]
        mxlen = max(len(x),len(y))
        x=''.join(['0']*(mxlen-len(x))) + x
        y=''.join(['0']*(mxlen-len(y))) + y
        dist = 0
        for i in range(mxlen):
            if x[i] != y[i]:
                dist += 1
        return dist            
