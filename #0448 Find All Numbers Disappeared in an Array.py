from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        Find all numbers from 1 to n that do not appear in the given list.

        Given a list of integers where each integer is between 1 and n (inclusive), 
        with some integers potentially missing, this method finds all the missing integers.

        Args:
        nums (List[int]): A list of integers where each integer is between 1 and n.

        Returns:
        List[int]: A list of integers that are missing from the given list.
        """
        results = []
        # Create a set of the numbers in the list for O(1) lookups
        nums_set = set(nums)

        # Check for each number from 1 to n if it is missing in the set
        for i in range(1, len(nums) + 1):
            if i not in nums_set:
                results.append(i)
        
        return results
