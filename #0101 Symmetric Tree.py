from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Check if a binary tree is symmetric (a mirror of itself).

        Args:
        root (Optional[TreeNode]): Root node of the binary tree.

        Returns:
        bool: True if the binary tree is symmetric, False otherwise.
        """
        # A tree is symmetric if the left subtree is a mirror reflection of the right subtree
        return self.isSymmetricAux(root.left, root.right) if root else True

    def isSymmetricAux(self, r1: Optional[TreeNode], r2: Optional[TreeNode]) -> bool:
        """
        Helper function to check if two trees are mirror images of each other.

        Args:
        r1 (Optional[TreeNode]): Root node of the first subtree.
        r2 (Optional[TreeNode]): Root node of the second subtree.

        Returns:
        bool: True if the two subtrees are mirror images of each other, False otherwise.
        """
        if not r1 and not r2:
            return True
        elif not r1 or not r2:
            return False
        return r1.val == r2.val and self.isSymmetricAux(r1.left, r2.right) and self.isSymmetricAux(r1.right, r2.left)
