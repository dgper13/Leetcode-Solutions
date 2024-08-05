from typing import List

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        """
        Count the number of seniors in the list of passenger details.

        Args:
        details (List[str]): A list where each string represents a passenger's details,
                             with age information in the 12th and 13th characters.

        Returns:
        int: The number of seniors (age > 60).
        """
        seniors = 0  # Initialize the count of seniors

        # Iterate over each passenger's details
        for passenger in details:
            # Extract the age part of the string (12th and 13th characters)
            age = int(passenger[11:13])
            
            # Check if the age is greater than 60
            if age > 60:
                seniors += 1  # Increment the count of seniors

        return seniors  # Return the total number of seniors
