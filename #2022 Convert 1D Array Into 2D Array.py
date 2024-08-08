from typing import List

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:

        total_elements = len(original)

        # If the total number of elements doesn't match the desired 2D array size, return an empty list
        if total_elements != m * n:
            return []

        result = []

        # Iterate through the original list in chunks of size 'n' to form each row of the 2D array
        for i in range(0, total_elements, n):
            result.append(original[i: i + n])
                
        return result
