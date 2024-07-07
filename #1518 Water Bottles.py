class Solution:
    def numWaterBottles(self, num_bottles: int, num_exchange: int) -> int:
        """
        Calculate the maximum number of water bottles you can drink.

        Given the number of full bottles you start with and the number of
        empty bottles required to exchange for a full bottle, this function
        calculates the total number of bottles you can drink.

        Args:
            num_bottles (int): Initial number of full water bottles.
            num_exchange (int): Number of empty bottles required to exchange for a full bottle.

        Returns:
            int: Total number of water bottles you can drink.
        """
        drank = 0
        empty_bottles = 0

        while num_bottles > 0:
            drank += num_bottles  # Drink all full bottles
            empty_bottles += num_bottles  # Collect empty bottles
            num_bottles = empty_bottles // num_exchange  # Exchange empty bottles for full ones
            empty_bottles = empty_bottles % num_exchange  # Remaining empty bottles after exchange
        
        return drank
