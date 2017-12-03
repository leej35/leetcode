class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans=[]
        for i in range(numRows):
            row=[1]
            if i > 1:
                for j in range(1,i):
                    n = ans[i-1][j-1] + ans[i-1][j]
                    row.append(n)
            if i > 0:
                row.append(1)
            ans.append(row)
        return ans
