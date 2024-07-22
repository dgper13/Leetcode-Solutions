class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Calculate the number of distinct ways to climb a staircase with `n` steps,
        where you can either take 1 or 2 steps at a time.

        Args:
        n (int): The total number of steps in the staircase.

        Returns:
        int: The number of distinct ways to reach the top.
        """
        # Base cases stored in a memoization dictionary
        memo = {1: 1, 2: 2}

        def f(x: int) -> int:
            """
            Recursive helper function to compute the number of ways to reach the `x`th step.
            
            Args:
            x (int): The current step.

            Returns:
            int: The number of ways to reach the `x`th step.
            """
            if x in memo:
                return memo[x]
            else:
                # Store the computed value in the memo dictionary
                memo[x] = f(x - 2) + f(x - 1)
                return memo[x]
        
        # Start the computation from step `n`
        return f(n)
