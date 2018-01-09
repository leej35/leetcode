class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        seen=set()
        
        def visit(r,c):
            if not ( 0<=r<len(grid) and 0<=c<len(grid[0]) and
                   grid[r][c]=='1' and (r,c) not in seen):
                return 0
            seen.add((r,c))
            visit(r+1,c)
            visit(r-1,c)
            visit(r,c+1)
            visit(r,c-1)
            return 1
        
        return sum(visit(r,c) for r in range(len(grid)) for c in range(len(grid[0])))
