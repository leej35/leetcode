class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        uc=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        wn=[1 if c in uc else 0 for c in list(word)]
        
        if sum(wn) == len(word) or sum(wn) == 0 or (wn[0] == 1 and sum(wn[1:]) == 0):
            return True
        return False
