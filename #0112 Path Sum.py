from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        Determine if the tree has a root-to-leaf path such that the sum of the values 
        along the path equals the targetSum.

        Args:
        root (Optional[TreeNode]): Root node of the binary tree.
        targetSum (int): Target sum to check against the path sums.

        Returns:
        bool: True if there exists a root-to-leaf path with the given sum, False otherwise.
        """
        # If the tree is empty, there cannot be any path
        if not root:
            return False
        
        # Subtract the value of the current node from the target sum
        targetSum -= root.val
        
        # Check if we have reached a leaf node and if the path sum equals the target sum
        if not root.left and not root.right:
            return targetSum == 0
        
        # Recursively check the left and right subtrees
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
