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
        longest_forward_valid_substring = 0
        current_substring = 0
        parenthesis_stack = []
        substring_length_stack = []
        for char in s:
            if char == '(':
                parenthesis_stack.append(char)
                if len(parenthesis_stack) > len(substring_length_stack) + 1:
                    substring_length_stack.append(current_substring)
                    current_substring = 0
            if char == ')':
                if parenthesis_stack:
                    parenthesis_stack.pop()
                    current_substring += 2
                    if len(parenthesis_stack) < len(substring_length_stack):
                        current_substring += substring_length_stack.pop()
                    longest_forward_valid_substring = max(longest_forward_valid_substring, current_substring)
                else:
                    current_substring = 0
        longest_forward_valid_substring = max(longest_forward_valid_substring, current_substring)
        return longest_forward_valid_substring

# Idea is we push current valid substring when we have pending left ps past a queue of 1. When the pending left p is closed, we add the current valid substring to the cached valid substring. 

