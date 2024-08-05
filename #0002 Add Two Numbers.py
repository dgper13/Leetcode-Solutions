from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Add two numbers represented by linked lists, where each node contains a single digit.
        The digits are stored in reverse order, so the 1's digit is at the head of the list.

        Args:
        l1 (Optional[ListNode]): The head of the first linked list representing the first number.
        l2 (Optional[ListNode]): The head of the second linked list representing the second number.

        Returns:
        Optional[ListNode]: The head of a new linked list representing the sum of the two numbers.
        """
        
        dummy = ListNode()  # Create a dummy node to simplify handling the result list
        tail = dummy        # Pointer to the current node in the result list
        carry = 0           # Carry value for sum calculation

        while l1 is not None or l2 is not None or carry != 0:
            # Start with the carry value
            digit = carry
            
            # Add the value from l1 if l1 is not None
            if l1 is not None:
                digit += l1.val
                l1 = l1.next
            
            # Add the value from l2 if l2 is not None
            if l2 is not None:
                digit += l2.val
                l2 = l2.next

            # Update carry and digit values
            carry = digit // 10
            digit = digit % 10

            # Create a new node with the digit and attach it to the result list
            tail.next = ListNode(digit)
            tail = tail.next  # Move the tail pointer to the newly added node

        return dummy.next  # Return the head of the result list
