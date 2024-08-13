# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass

class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        This function finds the first bad version among n versions.
        
        Args:
        n (int): The total number of versions.
        
        Returns:
        int: The version number of the first bad version.
        """
        low = 1
        high = n

        # Binary search loop to find the first bad version
        while low < high:  # Continue until low and high converge
            mid = low + (high - low) // 2  # Calculate the middle version
            
            # Check if mid version is bad
            if isBadVersion(mid):
                high = mid  # If mid is bad, then the first bad version is in the left half or might be mid itself
            else:
                low = mid + 1  # If mid is good, discard the left half and continue searching in the right half
        
        # At the end, low == high, and it points to the first bad version
        return low
