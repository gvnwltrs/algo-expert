
'''

Write a function that takes in a BST and a positive integer 'k' and returns the kth largest contained in BST. 
'''

class BST:

    # This is an input class. Do not edit.
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    # Write your code here.
    print(self.value)
    storage = []
    flat_box = flatten_tree(tree, storage) 
    # sort flat_box ascending
    flat_box.sort()
    return flat_box[-k]

def flatten_tree(node, container):
    container.append(node.value)

    if node.left is not None:
        flatten_tree(node.left, container)
    if node.right is not None:
        flatten_tree(node.right, container)

    return container 



