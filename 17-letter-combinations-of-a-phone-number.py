# class Solution(object):
#     def letterCombinations(self, digits):
#         """
#         :type digits: str
#         :rtype: List[str]
#         """
#         if digits=='': return []
        
#         map = {'1':'R','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        
        
#         res = ['']
#         asets = []
#         for digit in list(digits):
#             asets.append(list(map[digit]))
        
#         for aset in asets:
#             res = [r+a for r in res for a in aset]

#         return res
    

    class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits=='': return []
        
        map = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        
        
        res = ['']
        alldigit2chars = []
#         for digit in list(digits):
#             asets.append(list(map[digit]))
        
#         for aset in asets:
#             res = [r+a for r in res for a in aset]

        for digit in list(digits):
            alldigit2chars.append(list(map[digit]))
        
        
        for onedigit_chars in alldigit2chars:
            new_res = []
            for char in onedigit_chars:
                for r in res:
                    new_res.append(r+char)
            res = new_res

        return res

    # number of digits: N
    # max number of chars for a digit: M
    
    # Space Complexity:
    # - map: O(M*N)
    # - res: O(M^N)
    # - alldigit2chars : same as map

    # Time Complexity
    # - 1st for loop: O(N)
    # - 2nd-4th for loops : O(N*M*(M*N))
