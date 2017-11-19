class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def str2int(num):
            v=0
            for i, n in enumerate(list(num)):
                v+=int(n)*(10**(len(num)-(i+1)))
            return v
        return str(str2int(num1)+str2int(num2))
