from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        Determine if a singly linked list is a palindrome.

        Args:
        head (Optional[ListNode]): The head of the linked list.

        Returns:
        bool: True if the list is a palindrome, False otherwise.
        """
        # Initialize slow and fast pointers
        slow = head
        fast = head

        # Move fast pointer twice as fast as the slow pointer
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        # Reverse the second half of the linked list
        slow = self.reverse_linked_list(slow)
        fast = head

        # Compare the first and second halves
        while slow is not None:
            if slow.val != fast.val:
                return False
            slow = slow.next
            fast = fast.next

        return True

    def reverse_linked_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverse a linked list.

        Args:
        head (Optional[ListNode]): The head of the linked list.

        Returns:
        Optional[ListNode]: The new head of the reversed linked list.
        """
        prev = None
        current = head

        while current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        return prev
