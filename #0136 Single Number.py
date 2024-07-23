from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Find the element that appears exactly once in the list, where every other element appears exactly twice.

        This method uses bitwise XOR to find the unique number. The XOR operation between two same numbers is 0,
        and XOR with 0 keeps the number unchanged. Hence, XOR-ing all numbers will cancel out those appearing twice.

        Args:
        nums (List[int]): A list of integers where every element appears exactly twice except for one element.

        Returns:
        int: The element that appears exactly once in the list.
        """
        result = 0
        # XOR all numbers in the list
        for n in nums:
            result ^= n
        
        return result
