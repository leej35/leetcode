class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = bin(n)[2:]
        cnt = 0
        for i in range(len(n)):
            if n[i] == '1':
                cnt += 1
        return cnt
