class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        overflow = 0
        # [1,2,9]
        for i in range(len(digits)-1, -1, -1):
            if i==(len(digits)-1): digits[i]+=1 # [1,2,10]
                
            digits[i] += overflow # [1,3,10]
                        
            if digits[i] > 9: # 
                overflow = 1 
                digits[i] -= 10 # [1,2,0], of=1
            else:
                overflow = 0
            
            if overflow == 1 and i == 0:
                digits = [overflow] + digits 
                
            
        return digits
