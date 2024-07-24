from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        Remove all the nodes of the linked list that have Node.val == val.

        Args:
        head (Optional[ListNode]): The head of the singly linked list.
        val (int): The value to be removed from the linked list.

        Returns:
        Optional[ListNode]: The head of the modified linked list.
        """
        # Create a dummy node that points to the head of the list
        dummy = ListNode(next=head)
        prev = dummy
        curr = head

        # Traverse the list
        while curr:
            if curr.val == val:
                # If the current node needs to be removed, adjust the previous node's next pointer
                prev.next = curr.next
            else:
                # Otherwise, move the previous pointer to the current node
                prev = curr
            # Move to the next node in the list
            curr = curr.next

        # Return the head of the modified list (skipping the dummy node)
        return dummy.next
