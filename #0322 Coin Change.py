from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Calculate the minimum number of coins needed to make up a given amount.

        Args:
        coins (List[int]): A list of coin denominations.
        amount (int): The target amount.

        Returns:
        int: The minimum number of coins needed to make up the amount, or -1 if it is not possible.
        """
        # Sort the coins to optimize the process of breaking out of the loop early
        coins.sort()
        
        # Initialize a list to store the minimum number of coins for each amount up to the target amount
        dp = [0] * (amount + 1)

        # Iterate over each amount from 1 to the target amount
        for i in range(1, amount + 1):
            # Set the initial minimum number of coins to infinity for each amount
            minn = float('inf')

            # Check each coin to find the minimum number of coins required
            for coin in coins:
                diff = i - coin
                if diff < 0:
                    # Break out of the loop if the coin is larger than the current amount
                    break
                # Update the minimum number of coins needed for the current amount
                minn = min(minn, dp[diff] + 1)
            
            # Store the computed minimum number of coins in the dp array
            dp[i] = minn
        
        # If the target amount can be made up with the given coins, return the minimum number of coins
        # Otherwise, return -1 indicating that it is not possible
        if dp[amount] < float('inf'):
            return dp[amount]
        return -1
