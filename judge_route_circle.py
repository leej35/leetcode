class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        _pos = [0,0]
        _map = {'U':[1,0], 'D':[-1,0],'L':[0,-1],'R':[0,1]}
        for m in list(moves):
            _pos[0] += _map[m][0]
            _pos[1] += _map[m][1]
        if _pos == [0,0]:
            return True
        else:
            return False
            
