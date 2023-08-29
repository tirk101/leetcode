class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lst = []
        most = 0
        for i in s:
            if i in lst: 
                j = 0
                for j in range(len(lst)): 
                    if lst[j] == i: break
                if j != len(lst)-1: lst = lst[j+1:]
                else: lst = []
            lst.append(i)
            if len(lst) > most: most = len(lst)
        return most
