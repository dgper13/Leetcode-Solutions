from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Given the root of a binary tree, return the length of the diameter of the tree.
        The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
        This path may or may not pass through the root.

        Args:
        root (Optional[TreeNode]): The root of the binary tree.

        Returns:
        int: The diameter of the binary tree.
        """
        largest_diameter = [0]

        def dfs(node: Optional[TreeNode]) -> int:
            """
            Depth-first search helper function to calculate the height of the tree
            and update the diameter.

            Args:
            node (Optional[TreeNode]): The current node in the binary tree.

            Returns:
            int: The height of the current node.
            """
            if not node:
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            # Update the largest diameter found
            largest_diameter[0] = max(largest_diameter[0], left_height + right_height)

            # Return the height of the current node
            return 1 + max(left_height, right_height)

        # Start the DFS from the root
        dfs(root)

        return largest_diameter[0]
