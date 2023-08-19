class Solution(object):
    def romanToInt(self, s):
        roman_str = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        replace_str = {'IV':'I'*4, 'IX':'V'+'I'*4, 'XL':'X'*4, 'XC':'L'+'X'*4, 'CD':'C'*4, 'CM':'D'+'C'*4}
        for i in replace_str.keys(): s = s.replace(i, replace_str[i])
        return sum(roman_str[i] for i in s)
