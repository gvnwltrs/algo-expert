# This is the class of the input root. Do not edit it.
'''
Given a Binary Tree, we are asked to compute all of the branch sums of the tree and return them in an array, ordered from leftmost branch sum to rightmost branch sum. In a tree, a branch is a path that starts at the root node and ends at one of the leaf nodes. A branch sum means the sum of all values in a branch.
'''

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