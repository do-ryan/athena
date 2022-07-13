"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.



Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        return self.helper(s, 0)

    def helper(self, s: str, left_pending: int):
        longest = 0
        if not s:
            return 0
        for i, char in enumerate(s):
            if char == ")":
                if left_pending > 0:
                    left_pending -= 1
                    longest += 1
                if left_pending == 0:
                    return longest + self.helper(s[i+1::], 0)
            else:
                return max(longest + self.helper(s[i+1::], left_pending + 1), max(longest, self.helper(s[i+1::], left_pending + 1)))
                    
