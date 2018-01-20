class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m,n = len(obstacleGrid), len(obstacleGrid[0])
        a = [[0 for x in range(n+1)] for y in range(m+1)]
        a[0][1] = 1
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if not obstacleGrid[i-1][j-1]:
                    a[i][j] = a[i][j-1] + a[i-1][j]
        
        return a[-1][-1]
    
