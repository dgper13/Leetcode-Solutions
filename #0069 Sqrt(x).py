class Solution:
    def mySqrt(self, x: int) -> int:
        """
        Compute and return the integer square root of a non-negative integer x.

        Args:
        x (int): A non-negative integer.

        Returns:
        int: The integer square root of x.
        """
        low = 0
        high = x

        while low <= high:
            mid = low + (high - low) // 2
            product = mid * mid

            if product == x:
                return mid
            elif product < x:
                low = mid + 1
            else:
                high = mid - 1

        return high
