class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Convert a Roman numeral string to an integer.

        Roman numerals are represented by the following characters:
        - I: 1
        - V: 5
        - X: 10
        - L: 50
        - C: 100
        - D: 500
        - M: 1000

        Args:
        s (str): A Roman numeral string.

        Returns:
        int: The integer representation of the Roman numeral.
        """
        # Dictionary to map Roman numerals to their integer values
        convert = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        
        # Iterate over the string except the last character
        for i in range(len(s) - 1):
            current_value = convert[s[i]]
            next_value = convert[s[i + 1]]
            
            # If the current value is less than the next value, subtract it from the total
            if current_value < next_value:
                total -= current_value
            else:
                # Otherwise, add it to the total
                total += current_value
        
        # Add the value of the last character to the total
        total += convert[s[-1]]
        
        return total
