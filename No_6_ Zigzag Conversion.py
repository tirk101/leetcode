class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        lst = ["" for i in range(numRows)]
        idx = 0
        step = 1
        for i in range(len(s)):
            lst[idx] += s[i]
            if idx + step >= numRows : step = -1
            elif idx + step < 0: step = 1 
            idx += step
        ans = ""
        for i in lst: ans += i
        return ans
