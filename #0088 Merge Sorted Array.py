from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merges two sorted arrays into the first array in-place.

        Args:
        nums1 (List[int]): The first sorted array with enough space to hold the elements of nums2.
        m (int): The number of elements initialized in nums1.
        nums2 (List[int]): The second sorted array.
        n (int): The number of elements initialized in nums2.
        """
        # Index for the last position of merged array
        last = m + n - 1

        # Merge in reverse order
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                # Place the larger element in the correct position
                nums1[last] = nums1[m-1]
                m -= 1
            else:
                # Place the larger element in the correct position
                nums1[last] = nums2[n-1]
                n -= 1
                
            # Move to the next position
            last -= 1

        # If there are remaining elements in nums2, copy them
        while n > 0:
            nums1[last] = nums2[n-1]
            n -= 1
            last -= 1
