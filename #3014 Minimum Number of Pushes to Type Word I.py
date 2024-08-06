class Solution:
    def minimumPushes(self, word: str) -> int:
        """
        Calculate the minimum number of pushes required to type the word on a keyboard
        with a specified row size.

        Args:
        word (str): The input word.

        Returns:
        int: The minimum number of pushes required.
        """
        
        len_word = len(word)
        row_size = 8  # The number of characters that fit in one row

        # If the word length is less than or equal to the row size, return the length of the word
        if len_word <= row_size:
            return len_word

        total = row_size  # Initial pushes for the first row
        base_pushes = 1  # Initial base pushes for each row after the first
        full_rows = (len_word - row_size) // row_size  # Number of full rows after the first

        # Calculate pushes for full rows
        for i in range(full_rows):
            total += (1 + base_pushes) * row_size  # Pushes for each full row
            base_pushes += 1  # Increment base pushes for the next row
        
        # Calculate pushes for remaining characters that don't fill a full row
        remaining = (len_word - row_size) % row_size
        total += remaining * (1 + base_pushes)  # Pushes for the remaining characters

        return total
