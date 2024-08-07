from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Finds the duplicate number in an array where the numbers are between 1 and n (inclusive),
        and there is only one duplicate number but it can be repeated more than once.

        Args:
        nums (List[int]): The list of integers.

        Returns:
        int: The duplicate number.
        """
        
        # Initialize two pointers, both starting at the first element
        slow = fast = nums[0]

        # Phase 1: Find the intersection point of the two runners.
        while True:
            slow = nums[slow]  # Move slow pointer by one step
            fast = nums[nums[fast]]  # Move fast pointer by two steps
            if slow == fast:  # The pointers meet; there's a cycle
                break
        
        # Phase 2: Find the entrance to the cycle
        fast = nums[0]  # Move fast pointer to the start of the list
        while fast != slow:  # Move both pointers by one step until they meet
            fast = nums[fast]
            slow = nums[slow]

        return slow  # The position where they meet is the duplicate number
