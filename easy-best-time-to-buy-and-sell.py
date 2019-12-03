# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        state = False  # False: not buy yet, True: already purchased
        value = 0  # value of current stock
        ptr = 1
        profit = 0
        while(ptr < len(prices)):
            
            if not state and prices[ptr-1] < prices[ptr]:
                # not purchased yet & yesterday was cheaper => buy!
                value = prices[ptr-1]
                state = True
            
            if state and value < prices[ptr]:
                # already purchased & today is expensive => sell!
                profit += prices[ptr] - value
                state = False
            
            ptr += 1
            
        return profit
