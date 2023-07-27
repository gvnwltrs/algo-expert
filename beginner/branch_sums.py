# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    sums = []
    sumUpBranches(root, 0, sums)
    return sums

def sumUpBranches(node, runningSum, sums):
    if node is None:
        return

    sum = runningSum + node.value
    if node.left is None and node.right is None:
        sums.append(sum)
        return

    sumUpBranches(node.left, sum, sums)
    sumUpBranches(node.right, sum, sums)