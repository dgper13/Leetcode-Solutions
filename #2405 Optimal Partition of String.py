class Solution:
    def partitionString(self, s: str) -> int:
        """
        Count the number of partitions needed such that each partition
        contains unique characters from the input string s.
        
        Parameters:
        s (str): The input string from which partitions are formed.
        
        Returns:
        int: The number of partitions required.
        """
        unique_chars = set()  # Set to track unique characters in the current partition
        partition_count = 0    # Counter for the number of partitions

        for char in s:
            if char in unique_chars:
                partition_count += 1
                unique_chars.clear()  # Clear the set for the next partition
            unique_chars.add(char)

        # Return the total number of partitions required
        return partition_count + 1
