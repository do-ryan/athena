"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""

class Solution:
    def merge(self, a1, a2):
        ret_array = ""
        while a1 or a2:
            if not a1 or not a2: 
                ret_array += a1 + a2
                break
            if  a1[0] < a2[0]:
                ret_array += a1[0]
                a1 = a1[1::]
            else:
                ret_array += a2[0]
                a2 = a2[1::]
        return ret_array

    def mergesort(self, array):
        if len(array) == 1:
            return array
        return self.merge(self.mergesort(array[0:len(array)//2]), self.mergesort(array[len(array)//2::]))

    def isAnagram(self, s: str, t: str) -> bool:
        return self.mergesort(s) == self.mergesort(t)
