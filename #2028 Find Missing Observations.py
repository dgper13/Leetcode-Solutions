from typing import List

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        """
        Calculate the missing rolls to achieve the desired mean.

        Parameters:
        rolls (List[int]): The list of existing rolls.
        mean (int): The desired mean of all rolls including missing ones.
        n (int): The number of missing rolls.

        Returns:
        List[int]: A list of missing rolls or an empty list if it's not possible.
        """
        
        # Calculate the total target sum of all rolls (existing + missing)
        target_sum = mean * (len(rolls) + n) - sum(rolls)

        # Check if the target sum is achievable with n missing rolls
        if target_sum < n or target_sum > 6 * n:
            return []

        res = []

        # Distribute the target sum into the n missing rolls
        while target_sum:
            # Determine the next entry (must be between 1 and 6)
            next_entry = min(6, target_sum - n + 1)
            res.append(next_entry)
            target_sum -= next_entry
            n -= 1
        
        return res
