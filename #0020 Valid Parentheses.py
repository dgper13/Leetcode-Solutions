class Solution:
    def isValid(self, s: str) -> bool:
        """
        Determine if the input string s has valid parentheses.

        Args:
        s (str): Input string consisting of parentheses '(', ')', '[', ']', '{', '}'

        Returns:
        bool: True if the parentheses are valid, False otherwise.
        """
        # Mapping of opening to closing parentheses
        entries = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        
        stack = []

        for c in s:
            if c in entries:
                # Push corresponding closing bracket onto the stack
                stack.append(entries[c])
            else:
                # If stack is empty or the top of stack doesn't match current character
                if not stack or stack.pop() != c:
                    return False
        
        # Stack should be empty if all opening brackets had matching closing brackets
        return not stack
    