# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Find the lowest common ancestor (LCA) of two nodes in a binary search tree (BST).

        Args:
        root (TreeNode): The root node of the BST.
        p (TreeNode): The first node.
        q (TreeNode): The second node.

        Returns:
        TreeNode: The LCA node.
        """

        # Start traversing from the root node
        curr = root
        
        # Continue traversing the tree
        while curr:
            # If both nodes p and q are greater than current node, LCA is in the right subtree
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # If both nodes p and q are smaller than current node, LCA is in the left subtree
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            # If the nodes are on either side of the current node, current node is LCA
            else:
                return curr
