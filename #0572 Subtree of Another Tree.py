from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Determines if a binary tree subRoot is a subtree of binary tree root.

        Args:
        root (Optional[TreeNode]): The root node of the main binary tree.
        subRoot (Optional[TreeNode]): The root node of the subtree to check.

        Returns:
        bool: True if subRoot is a subtree of root, False otherwise.
        """
        if not root:
            return False
        
        # Check if the current node in root matches subRoot
        if self.isSameTree(root, subRoot):
            return True
        
        # Recursively check the left and right subtrees of root
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Check if two binary trees are identical.

        Args:
        p (Optional[TreeNode]): Root node of the first binary tree.
        q (Optional[TreeNode]): Root node of the second binary tree.

        Returns:
        bool: True if the two binary trees are identical, False otherwise.
        """
        # Base case: both trees are empty
        if not p and not q:
            return True
        # One tree is empty, the other is not
        elif not p or not q:
            return False
        # Both trees are not empty; compare their values and recursively check left and right subtrees
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
