class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        seq=[]
        for i in range(0,rowIndex+1):
            row=[1]
            if i > 0:
                for j in range(1,i):
                    n = seq[i-1][j-1] + seq[i-1][j]
                    row.append(n)
                row.append(1)
            seq.append(row)
            print row
        return seq[rowIndex]
