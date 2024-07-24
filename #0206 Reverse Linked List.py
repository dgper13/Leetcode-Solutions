from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverse a singly linked list.

        Args:
        head (Optional[ListNode]): The head of the singly linked list.

        Returns:
        Optional[ListNode]: The new head of the reversed singly linked list.
        """
        prev = None
        curr = head
        
        while curr:
            # Store the next node
            temp = curr.next
            # Reverse the current node's pointer
            curr.next = prev
            # Move the pointers one position ahead
            prev = curr
            curr = temp
        
        return prev
