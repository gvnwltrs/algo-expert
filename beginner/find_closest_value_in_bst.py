def findClosestValueInBst(tree, target):
    closest_value = tree.value
    
    while tree is not None:
        if abs(tree.value - target) < abs(closest_value - target):
                closest_value = tree.value
        if target == tree.value:
            return target
        elif tree.value < target:
            tree = tree.right
        elif tree.value > target:
            tree = tree.left
    
    return  closest_value


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None