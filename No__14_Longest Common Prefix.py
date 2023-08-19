class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = min(strs, key=len)
        for i in range(len(res)):
            if any(res[i] != s[i] for s in strs): return res[:i]
        return res
