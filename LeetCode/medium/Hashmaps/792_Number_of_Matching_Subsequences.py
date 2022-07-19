"""
Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".


Example 1:

Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
Example 2:

Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2


Constraints:

1 <= s.length <= 5 * 104
1 <= words.length <= 5000
1 <= words[i].length <= 50
s and words[i] consist of only lowercase English letters.
"""
from typing import List
from collections import defaultdict
'''
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # time exceeded
        matching_count = 0
        for char in s:
            for i, word in enumerate(words):
                if len(word) > 0:
                    if word[0] == char:
                        words[i] = words[i][1::]
                    if len(words[i]) == 0:
                        matching_count += 1
        return matching_count
'''

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        dict_partial_trie = defaultdict(list)
        for word in words:
            dict_partial_trie[word[0]].append(word)

        matching_count = 0
        for char in s:
            words = dict_partial_trie.get(char, [])
            dict_partial_trie[char] = []
            for i in range(len(words)):
                if len(words[i]) > 0:
                    if len(words[i]) == 1:
                        matching_count += 1
                    else:
                        dict_partial_trie[words[i][1]].append(words[i][1::])
        return matching_count


