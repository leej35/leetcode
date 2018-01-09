class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        seen = set()
        
        def visit(r,c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0]) and
                   (r,c) not in seen and grid[r][c]):
                return 0
            seen.add((r,c))
            return 1 + visit(r+1, c) + visit(r-1, c) + visit(r, c+1) + visit(r, c-1)
        
        return max(visit(r,c) for r in range(len(grid)) for c in range(len(grid[0])))
