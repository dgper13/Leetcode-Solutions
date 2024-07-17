from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        """
        Find the difference between two lists of integers.

        Args:
        nums1 (List[int]): First list of integers.
        nums2 (List[int]): Second list of integers.

        Returns:
        List[List[int]]: A list containing two sublists:
                         - Sublist 1: Elements in nums1 that are not in nums2.
                         - Sublist 2: Elements in nums2 that are not in nums1.
        """
        nums1 = set(nums1)  # Convert nums1 to a set to remove duplicates
        nums2 = set(nums2)  # Convert nums2 to a set to remove duplicates

        answer1 = []  # Initialize list to store elements in nums1 but not in nums2
        answer2 = []  # Initialize list to store elements in nums2 but not in nums1

        # Iterate through elements in nums1 to find differences
        for n1 in nums1:
            if n1 not in nums2:
                answer1.append(n1)  # Add n1 to answer1 if it's not in nums2

        # Iterate through elements in nums2 to find differences
        for n2 in nums2:
            if n2 not in nums1:
                answer2.append(n2)  # Add n2 to answer2 if it's not in nums1
        
        # Return a list containing answer1 and answer2 as sublists
        return [answer1, answer2]
