# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/880/
class Solution:
    def reverse(self, x: int) -> int:
        _x = str(x)
        if x < 0:
            ans = -int(_x[1:][::-1])
        else:
            ans = int(_x[::-1])
        if ans > 2**31 - 1 or ans < - 2**31:
            ans = 0
        return ans
