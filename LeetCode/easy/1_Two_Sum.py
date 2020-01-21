"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
from typing import List
from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dic = defaultdict(list)
        for i, num in enumerate(nums):
            num_dic[num].append(i)
        for num in num_dic:
           if target-num in num_dic and (num_dic[target-num] != num_dic[num] or len(num_dic[target-num]) > 1):
               return [num_dic[num][0], num_dic[target-num][-1]]
               
