from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Invert a binary tree recursively.

        Args:
        root (Optional[TreeNode]): Root node of the binary tree.

        Returns:
        Optional[TreeNode]: Root node of the inverted binary tree.
        """
        self.invertAux(root)
        return root
    
    def invertAux(self, root: Optional[TreeNode]):
        """
        Helper function to invert the binary tree recursively.

        Args:
        root (Optional[TreeNode]): Current node of the binary tree to be inverted.
        """
        if not root:
            return
        
        # Swap left and right children of the current node
        root.left, root.right = root.right, root.left
        
        # Recursively invert left and right subtrees
        self.invertAux(root.left)
        self.invertAux(root.right)
