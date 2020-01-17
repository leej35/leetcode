# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for c in s:
            if c not in d:
                d[c] = 0
            d[c] += 1
        
        for i, c in enumerate(s):
            if d[c] == 1:
                return i
        return -1
