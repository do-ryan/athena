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
def inp():
    n_pairs = int(input())
    pairs = []
    for _ in range(n_pairs):
        pairs.append((int(tok) for tok in input().split(' ')))
    return pairs

def find_n_length_with_k_ones(n, k, bit_patterns=[]):
    if k == 0:
        return ['0'*n]
    elif n == k:
        return ['1'*n]
    else:
        return ['1' + pat for pat in find_n_length_with_k_ones(n-1, k-1)] + ['0' + pat for pat in find_n_length_with_k_ones(n-1, k)]


if __name__ == "__main__":

    """
    Solution:
        - n choose k
        - intuition: start with n!, all the ways to scramble letters a_i for i in 1 to N.
        leters a in A start off in alphabetical order. Take the first k digits-
        in the scrambling process, we see all the different possible letter combinations, including same combinations for k with different orders. We divide n! by k! to eliminate all the different permutations of the same combinations. We divide again by (n-k)! to eliminate all the different permutations of the remaining letters (last n-k digits). As a result, the number of bit pattern combinations are n!/k!(n-k)!
        - to find all combinations, recursively try both values for each digit and return when k 0s are encountered. O(2^n)
        - O(min(n^k, n^(n-k)) solution: k loops of n times each and and find all distinct choices of n in k. the choices define where to place the 1s. skip when duplicate location is encountered. big memory use however possibly... 
    """
    n_ks = inp()
    for n, k in n_ks:
        print('The bit patterns are')
        for pattern in find_n_length_with_k_ones(n, k):
            print(pattern)
        print()
    pass
