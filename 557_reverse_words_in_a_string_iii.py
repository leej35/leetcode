class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ws = s.split(' ')
        _ws = []
        
        def rev(w):
            _w=''
            for c in list(w):
                _w = c + _w 
            return _w
        
        for w in ws:
            _ws.append(rev(w))
            
        return ' '.join(_ws)
