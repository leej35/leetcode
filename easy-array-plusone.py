# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 1
        
        for i in range(len(digits)):
            
            j = len(digits) - i - 1
            
            if digits[j] + carry >= 10:
                digits[j] = digits[j] + carry - 10
                carry = 1
            else:
                digits[j] += carry
                carry = 0
        
            # when carry is overflowing => add additional element
            if i == len(digits) - 1 and carry != 0:
                digits = [carry] + digits
        
        return digits
            
            
