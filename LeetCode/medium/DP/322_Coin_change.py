"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.



Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0


Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
"""

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        lowest_coins_cache = [0] + [10**5 for _ in range(amount)]
       
        for this_amount, lowest_coins in enumerate(lowest_coins_cache):
            for coin in coins:
                if coin == this_amount:
                    lowest_coins_cache[this_amount] = 1
                elif (this_amount + 1) - coin > 0:
                    lowest_coins_cache[this_amount] = min(lowest_coins_cache[this_amount], lowest_coins_cache[this_amount - coin] + 1)

        return lowest_coins_cache[-1] if lowest_coins_cache[-1] < 10**5 else -1 
