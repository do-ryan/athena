'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        lr_max_height = [0]
        rl_max_height = [0]
        for i in range(0, len(height), 1):
            lr_max_height.append(max(lr_max_height[-1], height[i]))
            rl_max_height.append(max(rl_max_height[-1], height[-1-i]))
        vol = 0
        for i in range(0, len(height), 1):
            vol += min(lr_max_height[i+1], rl_max_height[-1-i]) - height[i] 
        return vol
