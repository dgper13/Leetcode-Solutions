class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        """
        Determines the position of the pillow after a given amount of time in a game where the pillow is passed along a line of people.

        Args:
        n (int): The number of people in the game.
        time (int): The time elapsed.

        Returns:
        int: The position of the pillow.
        """
        # Calculate the length of one full cycle (forward and backward).
        cycle_length = 2 * (n - 1)
        
        # Calculate the position within the current cycle.
        position_in_cycle = time % cycle_length
        
        # Determine the position based on the current cycle position.
        if position_in_cycle <= n - 1:
            # If the position is in the forward pass (0 to n-1).
            return position_in_cycle + 1
        else:
            # If the position is in the backward pass (n-1 to 0).
            return 2 * (n - 1) - position_in_cycle + 1
