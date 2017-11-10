class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        a={}
        for c in list(t):
            if a.has_key(c):
                a[c]+=1
            else:
                a[c]=1

        for c in list(s):
            a[c]-=1
            if a[c] < 1:
                del a[c]
        
        return a.keys()[0]
