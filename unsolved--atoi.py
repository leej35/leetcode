#https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/884/
# almost there..but not yet.
class Solution:
    def myAtoi(self, x: str) -> int:
        nums = '1234567890'
        min_i = -2**31
        max_i = 2**31-1
        x = list(x)
        
        # remove trailing zero
        if ' ' in x:
            x.remove(' ')
        print(x[0])
        
        if len(x) < 1 or (x[0] not in nums and x[0] != '-'):
            return 0
        
        if '-' in x: # len(x) > 0 and x[0] == '-':
            sgn = -1
        else:
            sgn = 1
            
        x = [c for c in x if c in nums]
        
        x = int(''.join(x)) * sgn
        
        if x > max_i:
            return max_i
        elif x < min_i:
            return min_i
        return x
        
