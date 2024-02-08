 
def invertBinaryTree(tree):
    
    if tree is None:
        return
    else:
        invertBinaryTree(tree.left)
        invertBinaryTree(tree.right)
        tree.left, tree.right = tree.right, tree.left

    return tree
    


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None