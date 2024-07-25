class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        """
        Remove one occurrence of the digit from the number to get the largest possible result.

        This method iterates through the number, and whenever it finds the specified digit, 
        it creates a new number by removing that digit. It keeps track of the maximum 
        number possible after each removal.

        Args:
        number (str): The input number as a string.
        digit (str): The digit to be removed.

        Returns:
        str: The largest number possible after removing one occurrence of the specified digit.
        """
        max_number = ""
        for i in range(len(number)):
            if number[i] == digit:
                # Create a new number by removing the current digit
                # Update max_number with the maximum number found
                max_number = max(max_number, number[:i] + number[i+1:])
        return max_number
