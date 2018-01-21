class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic={}
        for token in strs:
            key=''.join(sorted(token))
            if dic.has_key(key):
                dic[key].append(token)
            else:
                dic[key] = [token]
        return dic.values()
