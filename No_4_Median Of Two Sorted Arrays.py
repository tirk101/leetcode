class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """  
        lst = sorted(nums1+nums2)
        median = 0
        half_idx = len(lst)/2
        if len(lst)%2: median = float(lst[half_idx])
        else: median = float(lst[half_idx] + lst[half_idx-1])/2
        return median
    
