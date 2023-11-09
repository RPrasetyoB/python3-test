# Maximum Depth of Binary Tree
# You are given a binary tree represented by its root node.
# Your task is to write a function,
# max_depth 
# that finds the maximum depth of the tree, which is the length of the longest path from the root node to a leaf node.
# Write a function called max_depth that takes the root node of the binary tree as its input and returns an integer representing the maximum depth.

import pytest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Function definition left intentionally empty for students to implement
def max_depth(root):
    if root is None:
        return 0
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    return max(left_depth, right_depth) + 1
    
    pass  # Students complete the implementation here

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    depth = max_depth(root)
    print("Maximum Depth:", depth)
# Do not modify this function call
retcode = pytest.main(['-v'])