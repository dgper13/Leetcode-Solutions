from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Detect if a linked list has a cycle in it.

        Parameters:
        head (Optional[ListNode]): The head of the singly linked list.

        Returns:
        bool: True if there is a cycle in the linked list, False otherwise.
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next       # Move slow pointer by one step
            fast = fast.next.next  # Move fast pointer by two steps

            if slow == fast:       # Cycle detected if slow and fast pointers meet
                return True

        return False               # No cycle found
