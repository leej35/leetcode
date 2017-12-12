class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        m = {}
        pattern = list(pattern)
        string = str.split(' ')
        if len(pattern) != len(string): return False
        for i, p in enumerate(pattern):
            if not m.has_key(p):
                if string[i] in m.values():
                    return False
                m[p] = string[i]

            if m[p] != string[i]:
                return False
        return True
