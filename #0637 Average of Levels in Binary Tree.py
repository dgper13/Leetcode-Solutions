from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        """
        Given the root of a binary tree, return the average value of the nodes on each level in the form of an array.

        Args:
        root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
        List[float]: A list of average values for each level of the binary tree.
        """
        results = []  # List to store the average of each level
        if not root:
            return results
        
        queue = [root]  # Initialize the queue with the root node

        while queue:
            level_sum = 0  # Sum of node values at the current level
            level_size = len(queue)  # Number of nodes at the current level

            for i in range(level_size):
                current_node = queue.pop(0)  # Dequeue the front node
                level_sum += current_node.val  # Add the node's value to the level sum
                if current_node.left:
                    queue.append(current_node.left)  # Enqueue left child
                if current_node.right:
                    queue.append(current_node.right)  # Enqueue right child
            
            results.append(level_sum / level_size)  # Calculate and store the average

        return results
