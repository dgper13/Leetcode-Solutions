from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Calculate the maximum depth of a binary tree.

        Args:
        root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
        int: The maximum depth of the binary tree.
        """
        if not root:
            return 0  # Base case: if root is None, return depth 0
        else:
            # Recursive case: return 1 (for the current node) + the maximum depth of its subtrees
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
