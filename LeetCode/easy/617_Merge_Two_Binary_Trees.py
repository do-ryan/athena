"""
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:

Input:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
Output:
Merged tree:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None and t2 is None:
            return None
        if t1 is None and t2 is not None:
            this_node = TreeNode(t2.val)
            this_node.left = self.mergeTrees(None, t2.left)
            this_node.right = self.mergeTrees(None, t2.right)
            return this_node
        if t1 is not None and t2 is None:
            this_node = TreeNode(t1.val)
            this_node.left = self.mergeTrees(t1.left, None)
            this_node.right = self.mergeTrees(t1.right, None)
            return this_node
        else:
            this_node = TreeNode(t1.val + t2.val)
            this_node.left = self.mergeTrees(t1.left, t2.left)
            this_node.right = self.mergeTrees(t1.right, t2.right)
            return this_node

