class Solution:
    def divisorGame(self, n: int) -> bool:
        """
        Determine if the starting player in the divisor game will win given the number n.

        In this game, players take turns to choose a number x such that 0 < x < n and n % x == 0.
        The player who cannot make a move loses the game. The game starts with the first player.

        Args:
        n (int): The initial number in the game.

        Returns:
        bool: True if the starting player will win, False otherwise.
        """
        # The starting player wins if and only if n is even
        return n % 2 == 0
