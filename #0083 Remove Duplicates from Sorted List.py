from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Remove duplicates from a sorted linked list.

        Args:
        head (Optional[ListNode]): The head of the sorted singly linked list.

        Returns:
        Optional[ListNode]: The head of the modified linked list with duplicates removed.
        """
        if not head:
            return head

        prev = head
        curr = head.next

        # Traverse the linked list
        while curr:
            if prev.val == curr.val:
                # Skip the current node if it's a duplicate
                prev.next = curr.next
            else:
                # Move prev to the current node if it's not a duplicate
                prev = curr
            # Move to the next node in the list
            curr = curr.next
        
        return head
