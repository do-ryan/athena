"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""
from typing import List

class Solution:
    def binary_search(self, lis: List[int], start: int, end: int, target:int) -> int:
        mid = (start + end) // 2
        if target == lis[mid]:
            return True

        if start == end:
            if target < lis[start]:
                return start-1
            else:
                return start

        if target < lis[mid]:
            return self.binary_search(lis, start, mid, target)
        elif target > lis[mid]:
            return self.binary_search(lis, mid+1, end, target)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        row_i = self.binary_search([row[0] for row in matrix], 0, len(matrix)-1, target)
        if type(row_i) is bool:
            return row_i
        else:
            return type(self.binary_search(matrix[row_i], 0, len(matrix[row_i])-1, target)) is bool
