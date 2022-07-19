"""
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.



Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
Example 2:

Input: n = 1, k = 1
Output: [[1]]


Constraints:

1 <= n <= 20
1 <= k <= n
"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        num_list = list(range(1, n+1, 1))
        ret_list = [[]]

        def dfs(num: int):
            ret_list[-1].append(num)
            if len(ret_list[-1]) < k:
                for num in num_list[num::]:
                    if num not in ret_list[-1]:
                        dfs(num)
                ret_list[-1].pop(-1)
            else:
                ret_list.append(ret_list[-1][0:-1])

        for num in num_list:
            dfs(num)
        ret_list.pop(-1)
        return ret_list
