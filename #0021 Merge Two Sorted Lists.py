from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge two sorted linked lists into a single sorted linked list.

        Args:
        list1 (Optional[ListNode]): The head of the first sorted singly linked list.
        list2 (Optional[ListNode]): The head of the second sorted singly linked list.

        Returns:
        Optional[ListNode]: The head of the merged sorted linked list.
        """
        # Create a dummy node to act as the start of the merged list.
        dummy = ListNode()
        curr = dummy

        # Iterate while both lists have nodes.
        while list1 and list2:
            # Compare the values of the nodes and append the smaller one to the merged list.
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            
            # Move the pointer of the merged list.
            curr = curr.next
            
        # If one list is exhausted, append the remaining nodes of the other list.
        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2
            
        # Return the head of the merged list.
        return dummy.next
