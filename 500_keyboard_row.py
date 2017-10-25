class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        r1 = list('qwertyuiop')
        r2 = list('asdfghjkl')
        r3 = list('zxcvbnm')
        rows = [r1,r2,r3]

        def word_checker(word,row):
            return reduce(lambda x,y: x*y, [c.lower() in row for c in list(word)])
                
        _ans = []
        for word in words:
            for row in rows:
                if word_checker(word, row):
                    _ans.append(word)
        return _ans
