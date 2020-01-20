"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""
import math

class Solution:
    def reverse(self, x: int) -> int:
        reversed = 0
        neg = False
        if x < 0:
            x *= -1
            neg = True
        elif x == 0:
            return 0
        n_dig = int(math.log(x, 10))
        for i in range(n_dig+1):
            reversed += x//10**(n_dig-i)*10**i
            x = x % 10**(n_dig-i) 
        if neg:
            reversed *= -1
        if abs(reversed) > 2**31 -1:
            return 0
        return reversed
