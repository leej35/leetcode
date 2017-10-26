class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        u_cd = list(set(candies))
        cd_n = [candies.count(c) for c in u_cd]
        sis = []
        i=0
        while len(sis) < len(candies)/2:
            if cd_n[i] > 0:
                sis.append(u_cd[i])
                cd_n[i] -= 1
            i = 0 if i+1 >= len(u_cd) else i+1
        return len(list(set(sis)))
                    
            
