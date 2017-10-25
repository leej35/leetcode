class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = bin(num)[2:]
        _num = []
        for n in list(num):
            _num.append('1' if n == '0' else '0')
        num = ''.join(_num)
        return int(num, 2)
