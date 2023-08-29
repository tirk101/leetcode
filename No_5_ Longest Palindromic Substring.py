class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        for i in range(len(s), 0, -1):
            for j in range(len(s)-i+1):
                ans = s[j:i+j]
                if ans == ans[::-1]: return ans
