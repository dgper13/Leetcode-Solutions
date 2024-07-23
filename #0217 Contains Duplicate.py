from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Check if there are any duplicate elements in the given list.

        Given a list of integers, this method determines if any value appears
        at least twice in the list. It returns True if any duplicates are found,
        and False otherwise.

        Args:
        nums (List[int]): A list of integers.

        Returns:
        bool: True if there are duplicates in the list, False otherwise.
        """
        # Initialize an empty set to track seen elements
        seen = set()

        # Iterate over each element in the list
        for n in nums:
            # If the element is already in the set, a duplicate is found
            if n in seen:
                return True
            # Add the element to the set
            seen.add(n)
        
        # No duplicates found, return False
        return False
