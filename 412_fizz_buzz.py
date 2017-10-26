class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        r = []
        for i in range(n):
            i = i+1
            if i%3 == 0 and i%5 == 0:
                s = 'FizzBuzz'
            elif i%3 == 0 and i%5 != 0:
                s = 'Fizz'
            elif i%5 == 0 and i%3 != 0:
                s = 'Buzz'
            else:
                s = str(i)
            r.append(s)
        return r
