class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        for i in range(1, len(s)+1):
            for j in range(0, len(s)-i+1):
                str = s[j:j+i]
                if str == str[::-1]:
                    count+=1
        return count
