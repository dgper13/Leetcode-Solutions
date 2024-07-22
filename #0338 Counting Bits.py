from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        Calculate the number of 1's in the binary representation of each number from 0 to n.

        Args:
        n (int): The upper limit of the range.

        Returns:
        List[int]: A list where the i-th element is the number of 1's in the binary representation of i.
        """
        # Initialize a list to store the number of 1's for each number from 0 to n
        dp = [0] * (n + 1)

        # Fill the dp list using the previously computed results
        for i in range(1, n + 1):
            # If i is even, the number of 1's is the same as in i // 2
            if i % 2 == 0:
                dp[i] = dp[i // 2]
            # If i is odd, the number of 1's is 1 plus the number of 1's in i // 2
            else:
                dp[i] = 1 + dp[i // 2]
        
        return dp
