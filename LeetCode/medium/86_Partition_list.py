"""
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.



Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]


Constraints:

The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None:
            return

        lis_left_part = []
        lis_right_part = []
        while head is not None:
            if head.val < x:
                lis_left_part.append(head)
            else:
                lis_right_part.append(head)
            head = head.next

        final_order = lis_left_part + lis_right_part
        current_head = final_order[0]
        output_head = current_head
        for node in final_order[1::]:
            current_head.next = node
            current_head = current_head.next
        current_head.next = None

        return output_head
