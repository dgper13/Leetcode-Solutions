from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Calculate the maximum profit that can be achieved by buying and selling stocks.

        Given a list of prices where each price represents the stock price on a given day,
        this method computes the maximum profit one can achieve by buying on one day and
        selling on a later day. 

        Args:
        prices (List[int]): A list of integers representing stock prices on different days.

        Returns:
        int: The maximum profit achievable. If no profit is possible, returns 0.
        """
        # If the prices list is empty, no profit can be made
        if not prices:
            return 0
        
        # Initialize the minimum price to the first price in the list
        min_value = prices[0]
        # Initialize the maximum profit to 0
        max_diff = 0

        # Iterate over each price in the list, starting from the second element
        for price in prices[1:]:
            # Calculate the potential profit for the current price
            max_diff = max(max_diff, price - min_value)
            # Update the minimum price if the current price is lower
            min_value = min(min_value, price)
        
        return max_diff
