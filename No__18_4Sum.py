class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums = sorted(nums)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                k = j + 1
                l = len(nums) - 1
                while k < l:
                    temp = nums[i] + nums[j] + nums[k] + nums[l]
                    if temp == target:
                        if [nums[i], nums[j], nums[k], nums[l]] not in res: 
                            res.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1
                    elif temp < target: k += 1
                    else: l -= 1
        return res
