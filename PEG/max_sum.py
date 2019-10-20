'''
Given an array of (positive) integers, find a subset with the maximal sum.
However, there is the additional restriction that no two numbers in the subset 
may be adjacent.

For example, for the array 4 5 6 9 10:
4 6 10 is valid, while 5 9 10 is invalid since 9 and 10 are next to each other.
4 6 10 happens to be the optimal sum in this case, so 20 is the answer.
Input
An integer 1 < N <= 100,000.
N lines, each with one positive integer in the sequence <= 1000
Output
The maximum sum possible.
'''

def inp():
    n = int(input())
    return [int(input()) for _ in range(n)]

if __name__ == '__main__':
    lis = inp()
    max_sum = [0]*len(lis)
    for i, item in enumerate(lis):
        if i == 0 or i == 1:
            max_sum[i] = item
        elif i == 2:
            max_sum[i] = item + max_sum[i-2]
        else:
            max_sum[i] = item + max(max_sum[i-2], max_sum[i-3]) 
    print(max(max_sum))
