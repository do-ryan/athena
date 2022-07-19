"""
15. 3Sum
Medium

19433

1856

Add to List

Share
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[1] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.


Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""
from typing import List
from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # create dictionary of 2sum: List[{index 1, index2}]
        # for each number, flip sign, and see if it exists as key in dictionary. append this number to each tuple in dict entry list.
        dict_2sum_tupleset = defaultdict(set)
        set_3sum = set()
        nums = sorted(nums)

        for i in range(len(nums)):
            if i <= 2 or nums[i] == 0 or (nums[i] != nums[i-1]):
                for j in range(len(nums)):
                    if i != j and (j <= 2 or nums[j] == 0 or (nums[j] != nums[j-2])):
                        dict_2sum_tupleset[nums[i] + nums[j]].add((min(i, j), max(i, j)))



                for tup in dict_2sum_tupleset[nums[i] * (-1)]:
                    if i != tup[0] and i != tup[1]:
                        if nums[tup[0]] > nums[tup[1]]:
                            tup = (tup[1], tup[0])
                        if nums[i] > nums[tup[1]]:
                            new_triple = (nums[tup[0]], nums[tup[1]], nums[i])
                        elif nums[i] < nums[tup[0]]:
                            new_triple = (nums[i], nums[tup[0]], nums[tup[1]])
                        else:
                            new_triple = (nums[tup[0]], nums[i], nums[tup[1]])

                        set_3sum.add(new_triple)

        return [list(trip) for trip in set_3sum]

