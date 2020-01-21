"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        works, ugly though.
        sequentially increase index by k and rotate values around. if loop detected, increase index by 1 and repeat. stop when number of passes is equal to length of list. need to ensure abs(index) is < len(list), 
        """
        next_i = 0
        if len(nums) != k:
            k %= len(nums)
        if k == 0 or len(nums) == k:
            return 
        j = 0
        while True:
            temp1 = nums[next_i]
            i = 0
            while True:
                if abs(next_i - (len(nums) - k)) <= len(nums)-1:
                    next_i -= len(nums) - k
                else:
                    next_i += k
                if j == len(nums) or ((len(nums) % k == 0) and i % (len(nums) // k) == 0 and i > 0):
                    # break loop
                    break
                elif len(nums) % (len(nums)-k) == 0 and i % (len(nums) // (len(nums)-k)) == 0 and  i > 0:
                    break
                temp0 = temp1
                temp1 = nums[next_i]
                nums[next_i] = temp0
                i += 1
                j += 1
            if next_i < -1:
                next_i += len(nums)
            next_i += 1
            if j == len(nums):
                break

    def rotate(self, nums: List[int], k: int) -> None:
        
    
