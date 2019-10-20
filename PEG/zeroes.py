'''
Task 3: Zeros
The factorial of a positive integer n, written as n!, is the product of the first n positive integers. That is,

n! = 1 × 2 × ... × n
Given a positive integer n, find the number of zeros in the decimal representation of n!. Of course, leading zeros should not be counted. (Note that decimal representation means base ten representation.)

Example 1. There are 7 zeros in the decimal representation of 20!.

20! = 1 × 2 × ... × 19 × 20 = 2432902008176640000

Example 2. There are 2 zeros in the decimal representation of 7!.
7! = 1 × 2 × 3 × 4 × 5 × 6 × 7 = 5040

Example 3. There is no zero in the decimal representation of 4!.
4! = 1 × 2 × 3 × 4 = 24

Input
The input contains a single positive integer n ≤ 100.

Output
The number of zeros in the decimal representation of n!.

Examples
Input
20

Output
7
Input
7

Output
2
Input
4

Output
0
'''

def inp():
    return int(input())
