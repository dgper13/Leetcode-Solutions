from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        Calculate the total sum of all root-to-leaf numbers.

        Args:
        root (Optional[TreeNode]): Root node of the binary tree.

        Returns:
        int: The total sum of all root-to-leaf numbers.
        """
        return self.sumAux(root, 0)
    
    def sumAux(self, root: Optional[TreeNode], current: int) -> int:
        """
        Helper function to calculate the sum recursively.

        Args:
        root (Optional[TreeNode]): Current node in the binary tree.
        current (int): Current value of the path number.

        Returns:
        int: The sum of all root-to-leaf numbers from the current node.
        """
        if not root:
            return 0

        # Update the current path value
        current = current * 10 + root.val

        # If the current node is a leaf, return the current path value
        if not root.left and not root.right:
            return current

        # Recursively calculate the sum for the left and right subtrees
        return self.sumAux(root.left, current) + self.sumAux(root.right, current)
