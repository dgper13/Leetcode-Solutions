class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        """
        Find the k-th factor of a given number n.
        
        Parameters:
        n (int): The number whose factors are to be considered.
        k (int): The 1-based index of the factor to be returned.
        
        Returns:
        int: The k-th factor of n if it exists, otherwise -1.
        """
        counter = 0
        sqrt_n = int(n**0.5)

        # First loop to find factors up to sqrt(n)
        for i in range(1, sqrt_n + 1):
            if n % i == 0:
                counter += 1
                if counter == k:
                    return i

        # Second loop to find factors greater than sqrt(n)
        for i in range(sqrt_n, 0, -1):
            if n % i == 0 and i != n // i:
                # To avoid counting the sqrt twice when n is a perfect square.
                counter += 1
                if counter == k:
                    # a*b = n  =>  b = n/a
                    return n // i

        return -1
