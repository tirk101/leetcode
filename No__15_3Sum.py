class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums = sorted(nums)
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                temp = nums[i] + nums[j] + nums[k]
                if temp == 0:
                    if [nums[i], nums[j], nums[k]] not in res: res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif temp < 0: j += 1
                else: k -= 1
        return res
