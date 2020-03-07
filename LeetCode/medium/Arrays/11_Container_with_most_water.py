"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""
from typing import List

class Solution:
    def maxAreaOld(self, height: List[int]) -> int:
        """O(max(height)*n)"""
        maxarea = 0
        for level in range(max(height)+1):
            this_first = -1
            this_last = -1
            for i, line in enumerate(height):
                if line >= level and this_first == -1:
                    this_first = i
                elif line >= level and this_first >= 0:
                    this_last = i
            maxarea = max(maxarea, level * (this_last - this_first))
        return maxarea 
                
    def maxArea(self, height: List[int]) -> int:
        """O(n)"""
        maxarea = 0
        left = 0
        right = len(height)-1
        while left < right:
         maxarea = max(maxarea, (right-left)*min(height[right], height[left])) 
         if height[left] < height[right]:
             left += 1
         else:
             right -= 1
        return maxarea
