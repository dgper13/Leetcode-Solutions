from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        """
        Summary ranges for a sorted list of unique integers.

        Given a sorted list of unique integers, this method returns the smallest 
        sorted list of ranges that cover all the numbers in the array exactly. 
        A range is represented in the format "a->b" if a != b, and "a" if a == b.

        Args:
        nums (List[int]): The input list of sorted unique integers.

        Returns:
        List[str]: A list of strings representing the summary ranges.
        """
        
        if not nums:
            return []

        ranges = []
        start = nums[0]

        for i in range(1, len(nums)):
            # If the current number is not consecutive, finalize the current range
            if nums[i] != nums[i - 1] + 1:
                if start == nums[i - 1]:
                    ranges.append(f"{start}")
                else:
                    ranges.append(f"{start}->{nums[i - 1]}")
                # Start a new range
                start = nums[i]

        # Finalize the last range
        if start == nums[-1]:
            ranges.append(f"{start}")
        else:
            ranges.append(f"{start}->{nums[-1]}")

        return ranges
