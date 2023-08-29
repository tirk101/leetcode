class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        paren = {'(':')', '[':']', '{':'}'}
        stack = []
        for i in s:
            if i in paren.keys(): stack.append(i)
            else:
                if not stack: return False
                else:
                    if paren[stack[-1]] == i: stack = stack[:-1]
                    else: return False
        return True if not stack else False
