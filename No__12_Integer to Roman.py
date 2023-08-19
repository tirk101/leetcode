class Solution(object):
    def intToRoman(self, num):
        roman = ""
        roman_str = {1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X', 40:'XL', 50:'L', 
                     90:'XC', 100:'C', 400:'CD', 500:'D', 900:'CM',1000:'M'}
        for i in sorted(roman_str.keys())[::-1]:
            while num >= i:
                roman += roman_str[i]
                num -= i 
        return roman
