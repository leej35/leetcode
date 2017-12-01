class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x=bin(x)[2:]
        y=bin(y)[2:]
        lx,ly=len(x),len(y)
        lmax,lmin=max(lx,ly),min(lx,ly)
        x='0'*(lmax-lx)+x
        y='0'*(lmax-ly)+y
        return sum([x[i]!=y[i] for i in range(lmax)])

"""
key idea: change input int to binary number by using bin() and zero padding, and compare difference.

"""
