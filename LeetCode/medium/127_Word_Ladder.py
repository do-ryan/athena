"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""
from typing import List
from collections import defaultdict

class Solution:
    def buildTransformGraph(self, wordList: List[str]):
        transform_dict = [defaultdict(list) for _ in range(len(wordList[0]))]
        for word in wordList:
            for i in range(len(word)):
                transform_dict[i][word[0:i] + word[i+1:]].append(word)
        # O(WL) where W is num words and L is length of each word
        
        graph_dict = defaultdict(set)
        for position in transform_dict:
            for neighbours in position.values():
                for word in neighbours:
                    graph_dict[word] = graph_dict[word].union(set(neighbours) - {word})
        return graph_dict


    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = self.buildTransformGraph(wordList + [beginWord])
        
        bfs_queue = [beginWord]
        distance = {beginWord: 1}
        for word in bfs_queue:
            next_distance = distance[word] + 1
            for neighbour in graph[word]:
                if distance.get(neighbour, -1) == -1 or distance.get(neighbour, -1) > next_distance:
                    bfs_queue.append(neighbour)
                    distance[neighbour] = next_distance
        
        return distance.get(endWord, 0)
