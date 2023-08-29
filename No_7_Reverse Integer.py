class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1
        if x<0: 
            sign = -1
            x = abs(x)
        while not x%10 and x:
            x /= 10 
        ans = int(str(x)[::-1]) * sign
        return 0 if ans> pow(2, 31)-1 or ans<pow(-2, 31) else ans
