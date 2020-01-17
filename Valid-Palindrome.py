#https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        abts = 'abcdefghijklmnopqrstuvwxyz0123456789'
        s = [c.lower() for c in s if c.lower() in abts]
        for i in range(int(len(s)/2)):
            if s[i] != s[-(i+1)]:
                return False
        return True
