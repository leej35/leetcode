import sys
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.list.append((x, min(x, self.getMin())))

    def pop(self):
        """
        :rtype: void
        """
        self.list.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.list:
            return self.list[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if self.list:
            return self.list[-1][1]
        return sys.maxint


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
