from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        Calculates the minimum path sum from top to bottom in a triangle array.
        
        Args:
        triangle (List[List[int]]): 2D list where each element represents a level in the triangle.
        
        Returns:
        int: The minimum path sum from top to bottom.
        """
        n = len(triangle)
        
        # Initialize the DP array with the last row of the triangle
        dp = triangle[-1]
        
        # Perform bottom-up calculation
        for row in range(n-2, -1, -1):  # Start from the second-last row and move upwards
            for i in range(len(triangle[row])):
                # Update dp[i] to be the current value plus the minimum of the two adjacent values from the row below
                dp[i] = triangle[row][i] + min(dp[i], dp[i+1])
        
        # The result is the minimum path sum from the top
        return dp[0]
