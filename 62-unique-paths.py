class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        a = [[1 for y in range(n) ] for x in range(m) ]
        for i in range(1,m):
            for j in range(1,n):
                a[i][j] = a[i-1][j]+a[i][j-1]
        return a[-1][-1]
