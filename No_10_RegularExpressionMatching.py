class Solution(object):
    def isMatch(self, s, p):
        memoize = {}
        def recursive(i, j):
            if (i, j) in memoize: return memoize[(i, j)]
            if i >= len(s) and j >= len(p): return True
            if j >= len(p): return False

            check = True if i < len(s) and (s[i] == p[j] or p[j] == '.') else False
            if j+1 < len(p) and p[j+1] == '*': 
                memoize[(i, j)] = recursive(i, j+2) or (check and recursive(i+1, j))
                return memoize[(i, j)]
            if check: 
                memoize[(i, j)] = recursive(i+1, j+1)
                return memoize[(i, j)] 
            memoize[(i, j)] = False
            return False

        return recursive(0, 0)
