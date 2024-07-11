from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Group anagrams from a list of strings.

        Parameters:
        strs (List[str]): A list of strings to be grouped.

        Returns:
        List[List[str]]: A list of lists, where each sublist contains anagrams.
        """
        groups = {}  # Dictionary to store grouped anagrams

        for s in strs:
            # Create a key by sorting the characters of the string and converting it to a tuple
            key = tuple(sorted(s))
            if key in groups:
                groups[key].append(s)  # Add the string to the existing group
            else:
                groups[key] = [s]  # Create a new group with the string

        return list(groups.values())  # Return the list of grouped anagrams
