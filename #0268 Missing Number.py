from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Find the missing number in a list containing numbers from 0 to n.

        Given a list of integers where each number from 0 to n appears exactly once
        except for one number that is missing, this method returns the missing number.

        Args:
        nums (List[int]): A list of integers where each number from 0 to n is present
                          except for one missing number.

        Returns:
        int: The missing number in the list.
        """
        length = len(nums)
        # Calculate the expected total sum of numbers from 0 to n
        expected_total = length * (length + 1) // 2
        # Subtract the sum of the given numbers from the expected total
        return expected_total - sum(nums)
