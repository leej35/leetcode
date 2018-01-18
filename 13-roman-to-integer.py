class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        map={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        prev_num = v = 0
        
        for i in range(len(s)-1,-1,-1):
            num = map[s[i]]
            if num < prev_num:
                v -= num
            else:
                v += num
                
            prev_num = num
        
        return v
