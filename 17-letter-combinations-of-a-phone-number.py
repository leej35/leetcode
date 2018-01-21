class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits=='': return []
        
        map = {'1':'R','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        
        
        res = ['']
        asets = []
        for digit in list(digits):
            asets.append(list(map[digit]))
        
        for aset in asets:
            res = [r+a for r in res for a in aset]

        return res
    
