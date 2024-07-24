from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Find the middle node of a singly linked list. If the list has an even number of nodes, return the second middle node.

        Args:
        head (Optional[ListNode]): The head of the singly linked list.

        Returns:
        Optional[ListNode]: The middle node of the linked list.
        """
        # Find the total number of nodes in the list
        middle = self.get_middle(head) // 2

        # Traverse to the middle node
        for _ in range(middle):
            head = head.next
        
        return head
    
    def get_middle(self, head: Optional[ListNode]) -> int:
        """
        Count the total number of nodes in the singly linked list.

        Args:
        head (Optional[ListNode]): The head of the singly linked list.

        Returns:
        int: The total number of nodes in the linked list.
        """
        right = 1
        while head.next:
            right += 1
            head = head.next
        return right
