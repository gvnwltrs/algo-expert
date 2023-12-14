
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
    if values is None or values[1] is None:
        return
    next_node = BST(values.pop(0))

    if next_node.value < root.value:
        root.left = next_node.value
        createBst(next_node, values)

    if root.value > root.value:
        root.right = next_node.value
        createBst(next_node, values)

    return root
