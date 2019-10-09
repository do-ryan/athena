"""
Given an array of integers, find the longest increasing subsequence.
A subsequence is just a collection of numbers from the array - however, they must be in order.

For example:
Array: 1 2 5 4 3 6
The longest increasing subsequence here is 1 2 5 6 (or 1 2 4 6, or 1 2 3 6).
The numbers must be strictly increasing - no two numbers can be equal.
Input
N <= 5000, the number of integers.
N lines, each with a value in the array.
Output
The length of the longest increasing subsequence of the array.

Sample input:
6
1
2
5
4
3
6
"""
import datetime


def inp():
    """Return list of integers from problem input"""
    n = int(input())
    ret = [int(input()) for _ in range(n)]
    # ret = []
    # marker = datetime.datetime.now()
    # for _ in range(n):
    # print(datetime.datetime.now() - marker)
    # marker = datetime.datetime.now()
    # ret.append(int(input()))
    return ret, n


def longest_increasing_subsequence(integers, n):
    """Return integer length of longest increasing subsequence from an ordered list of integers.

    Dynamic programming.
    """

    if n < 1:
        return 0

    lis = [1 for _ in integers]

    for i in range(1, n):
        for j in range(i):
            if integers[i] > integers[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    return max(lis)


print(longest_increasing_subsequence(ret, n))
