class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ## key idea: create map of unique character to numbers
        ## and change string to a numbers.
        
        def str2num(word):
            m,w = {},''
            for c in list(word):
                if not m.has_key(c):
                    m[c]=len(m.keys())
                w+=str(m[c])
            return w

        return str2num(s) == str2num(t)
