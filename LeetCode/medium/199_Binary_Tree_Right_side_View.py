"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        bfs_queue = [root]
        distance_dict = {root: 1}
        right_list = []
        next_distance = 0
        if root is None:
            return None

        while len(bfs_queue) > 0:
            if distance_dict[bfs_queue[0]] == next_distance: # if the next node is in a new level
                right_list.append(this_node.val) # add the last node of last level
            this_node = bfs_queue.pop(0) # dequeue the next node into this node
            next_distance = distance_dict[this_node] + 1 # update next distance
            for node in [this_node.left, this_node.right]: # for children
                if node is not None: 
                    bfs_queue.append(node) # add to bfs queue each child
                    distance_dict[node] = next_distance # assign next distance to each child
        right_list.append(this_node.val) # add last leaf node
        return right_list
                

