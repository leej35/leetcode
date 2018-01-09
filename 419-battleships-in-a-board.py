class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        seen=set()
        def visit(r,c):
            if ( 0<=r<len(board) and 0<=c<len(board[0]) and board[r][c] == "X" and (r,c) not in seen):
                seen.add((r,c))
                visit(r+1,c)
                visit(r-1,c)
                visit(r,c+1)
                visit(r,c-1)
                return 1
            else:
                return 0
                
        return sum(visit(r,c) for r in range(len(board)) for c in range(len(board[0])))
