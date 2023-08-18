class Solution(object):
    def maxArea(self, height):
        area = 0
        i = 0
        j = len(height) - 1

        while(j > i):
            temp_idx = j - i
            if height[i] < height[j]:
                temp_min = height[i]
                i += 1
            else:
                temp_min = height[j]
                j -= 1
            temp_area = temp_min * temp_idx
            area = max(temp_area, area)
        return area
