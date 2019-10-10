"""
2003 Canadian Computing Competition, Stage 1
Problem S4: Substrings
How many distinct substrings does a given string S have?

For example, if S = "abc", S has 7 distinct substrings: "", "a", "b", "c", "ab", "bc", "abc".
Note that the empty string and S itself are considered substrings of s.

On the other hand, if S = "aaa". S has only 4 distinct substrings: "", "a", "aa", "aaa".

Input
The first line of the input file contains N, the number of test cases. For each test case, a line follows giving S,
a string of from 1 to 5000 alphanumeric characters.

Output
Your output consists of one line per case, giving the number of distinct substrings of S.

Grading
50% of test cases will have l (the length of the string) ≤ 1,000.
For all cases, l ≤ 5000.
Sample Input
2
abc
aaa
Sample Output
7
4
"""