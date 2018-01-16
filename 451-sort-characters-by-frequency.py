class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        h = {}
        # 1. count frequency
        for c in list(s):
            if not h.has_key(c):
                h[c] = 1
            else:
                h[c] += 1

        # 2. sort characters
        l = [(v,k) for k,v in h.iteritems()]
        z = sorted(l, key=lambda x: x[0], reverse=True)

        # 3. compile result into a string
        r = []
        r += [k*v for (v,k) in z]
        return ''.join(r)
