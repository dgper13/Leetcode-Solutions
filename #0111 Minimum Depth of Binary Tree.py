from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """
        Returns the minimum depth of a binary tree.
        The minimum depth is the number of nodes along the shortest path from 
        the root node down to the nearest leaf node.

        Args:
        root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
        int: The minimum depth of the binary tree.
        """
        if not root:
            return 0

        # Initialize a queue for breadth-first search (BFS)
        queue = [root]
        depth = 1
        
        # Perform BFS
        while queue:
            # Iterate over all nodes at the current depth
            for _ in range(len(queue)):
                n = queue.pop(0)
                
                # Check if the current node is a leaf node
                if not n.left and not n.right:
                    return depth
                
                # Add child nodes to the queue
                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)
            
            # Increment the depth after processing the current level
            depth += 1
        
        return 0
