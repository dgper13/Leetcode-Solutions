from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Given the root of a binary tree, return the values of the nodes you can see ordered from top to bottom 
        when looking at the tree from the right side.

        Args:
        root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
        List[int]: A list of node values visible from the right side.
        """
        results = []  # List to store the rightmost values at each level
        if not root:
            return results
        
        queue = [root]  # Initialize the queue with the root node

        while queue:
            number_of_nodes = len(queue)  # Number of nodes at the current level

            for i in range(number_of_nodes):
                current = queue.pop(0)  # Dequeue the front node
                if i == number_of_nodes - 1:
                    # Add the value of the rightmost node at the current level to the results
                    results.append(current.val)
                
                # Enqueue the left and right children if they exist
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
        
        return results
