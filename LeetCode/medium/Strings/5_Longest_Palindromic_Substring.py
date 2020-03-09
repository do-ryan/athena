"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            if i+1 < len(s): 
                if s[i+1] != s[i]:
                    p2_l = [i]
                else: 
                    p2_l = [i, i+1]
            else:
                p2_l = [i]
            for p2 in p2_l:
                p1 = i
                while p1 >= 0 and p2 < len(s) and s[p1] == s[p2]:
                    this_substring = s[p1:p2+1]
                    if len(this_substring) > len(longest):
                        longest = this_substring
                    p1 -= 1
                    p2 += 1
        return longest
