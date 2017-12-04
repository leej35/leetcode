class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """ key idea: i = (sub)seqlen
            loop over seqlen from 1 to the half of the length of input. 
            only if len(s) / seqlen == 0, check whether each subseqences are same.
        """
        for i in range(1, len(s)/2+1):
            if len(s) % i == 0:
                n_seg = len(s) / i
                b = 1
                for j in range(0,n_seg-1):
                    b *= s[j*i : (j+1)*i] == s[(j+1)*i : (j+2)*i]
                if b:
                    return True
        return False
