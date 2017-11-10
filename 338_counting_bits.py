class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        r=[]
        for i in range(num+1):
            s=bin(i)[2:]
            n=0
            for c in list(s):
                n+=int(c)
            r.append(n)
        return r
