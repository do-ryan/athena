"""
1996 Canadian Computing Competition, Stage 1
Problem C: Pattern Generator
Write a program that repeatedly reads two numbers n and k and prints all bit patterns of length n with k ones
in descending order (when the bit patterns are considered as binary numbers). You may assume that 30 ≥ n > 0, 8 > k ≥ 0,
and n ≥ k. The first number in the input gives the number of pairs n and k.
The numbers n and k are separated by a single space. Leading zeroes in a bit pattern should be included.
See the example below.

Sample Input
3
2 1
2 0
4 2

Sample Output
The bit patterns are
10
01

The bit patterns are
00

The bit patterns are
1100
1010
1001
0110
0101
0011
"""

if __name__ == "__main__":
    """
    Solution:
        - n choose k
