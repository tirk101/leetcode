class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def combi(digits, res=[]):
            if not digits: return res
            temp = letter_dict[digits[0]]
            new_res = []
            if res:            
                for i in res:
                    for j in temp:
                        new_res.append(i+j)
            else: new_res = temp
            return combi(digits[1:], new_res)
        
        letter_dict = {'2':['a', 'b', 'c'], '3':['d', 'e', 'f'], '4':['g', 'h', 'i'], '5':['j', 'k', 'l']
                     , '6':['m', 'n', 'o'], '7':['p', 'q', 'r', 's'], '8':['t', 'u', 'v'], '9':['w', 'x', 'y', 'z']}
        
        return combi(digits)
