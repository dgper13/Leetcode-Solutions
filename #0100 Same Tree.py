from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
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
