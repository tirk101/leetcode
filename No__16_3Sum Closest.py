class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def min_difference(num1, num2):
            return num1 if abs(num1 - target) < abs(num2 - target) else num2
        nums = sorted(nums)
        res = sum(nums[:3])
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                temp = nums[i] + nums[j] + nums[k]
                if temp == target: return target
                elif temp < target:
                    res = min_difference(temp, res)
                    j += 1
                else:
                    res = min_difference(temp, res)
                    k -= 1                    
        return res
