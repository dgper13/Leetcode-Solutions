from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        """
        Determine if each kid can have the greatest number of candies if they receive
        extra candies.

        Args:
        candies (List[int]): A list of integers representing the number of candies each kid has.
        extraCandies (int): The number of extra candies each kid can receive.

        Returns:
        List[bool]: A list of booleans where each boolean represents whether a kid can have
                    the greatest number of candies after receiving extra candies.
        """
        
        current_max = max(candies)  # Find the current maximum number of candies any kid has

        results = []  # Initialize an empty list to store the results

        # Iterate through each kid's candies
        for candies_count in candies:
            # Check if the current kid can have the greatest number of candies with extra candies
            if candies_count + extraCandies >= current_max:
                results.append(True)  # Add True to the results if the condition is met
            else:
                results.append(False)  # Add False to the results if the condition is not met
        
        return results  # Return the list of results
