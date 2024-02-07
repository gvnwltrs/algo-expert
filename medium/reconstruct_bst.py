
# Problem: the pre-order traversal of a Binary Tree is a traversal technique
# that starts at teh tree's root node and vists nodes in the following order:
#   1. current node
#   2. left subtree
#   3. right subtree
# Given a non-empty array of integers representing the pre-order preOrderTraversalValues
# of a Binary Search Tree (BST), write a fucntion that creates the relevant BST and 
# returns its root node. 


# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preOrderTraversalValues):
    return createBst(BST(preOrderTraversalValues.pop(0)), preOrderTraversalValues)

def createBst(root, values):
    root = BST(preOrderTraversalValues[0])
    left_tree = []
    right_tree = []
    for node_value in preOrderTraversalValues[1:]: #O(n-1)
        if node_value < root.value:
            left_tree.append(node_value)
        else:
            right_tree.append(node_value)

    if left_tree:
        root.left = reconstructBst(left_tree)
    if right_tree:
        root.right = reconstructBst(right_tree)
        
    return root
