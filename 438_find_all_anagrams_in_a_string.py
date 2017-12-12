from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        pC = Counter(p)
        sC = Counter(s[:len(p)-1])
        print s[:len(p)-1]
        ## Key idea : number of characters are met, it is anagram!
        ## SO having a sliding window, size of len(p), and compare.        
        ## To speed up, make the sliding window on the fly by adding and removing first and last
        ## character respectively.
        ans = []
        for i in range( len(s)-len(p)+1 ):
            sC[s[i+len(p)-1]] += 1
            if pC == sC:
                ans.append(i)
            sC[s[i]] -= 1
            if sC[s[i]] == 0:
                del sC[s[i]]
        return ans
