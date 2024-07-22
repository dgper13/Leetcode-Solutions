from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        """
        Given a list of names and their corresponding heights, sort the names based on heights in descending order.

        Args:
        names (List[str]): A list of names.
        heights (List[int]): A list of heights corresponding to the names.

        Returns:
        List[str]: A list of names sorted by heights in descending order.
        """
        # Combine names and heights into a list of tuples
        combined = list(zip(names, heights))
        
        # Sort the combined list based on heights in descending order
        sorted_combined = sorted(combined, key=lambda x: x[1], reverse=True)
        
        # Extract the sorted names
        result = []
        for name, height in sorted_combined:
            result.append(name)
        
        return result
    