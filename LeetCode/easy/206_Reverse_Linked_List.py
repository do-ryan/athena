"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    root = None
    def reverseList(self, head: ListNode) -> ListNode:
        """Recursively reverse linked list."""
        if head is None:
            return
        if head.next is None:
            global root
            root = head
            return root
        self.reverseList(head.next)
        if head.next.next is None:
            head.next.next = head
            head.next = None
        return root

   def reverseList(self, head: ListNode) -> ListNode:
        """Iteratively reverse linked list."""
        prev = None
        curr = head
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
