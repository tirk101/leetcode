class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        sign = 1
        nums = ['0','1','2','3','4','5','6','7','8','9']
        temp = ""
        for i in s:
            if i in nums: 
                temp += i
                if len(temp) > 1 and temp[0] == nums[0]: temp = temp[1:]
            elif i == '-' and not temp and s.index(i) != len(s)-1 and s[s.index(i)+1] in nums: sign = -1
            elif i == '+' and not temp and s.index(i) != len(s)-1 and s[s.index(i)+1] in nums: continue
            elif i == ' ' and not temp: continue
            else: break
        ans = int(temp) * sign if temp else 0
        if ans<pow(-2, 31): ans = pow(-2, 31) 
        if ans> pow(2, 31)-1: ans = pow(2, 31)-1 
        return ans
