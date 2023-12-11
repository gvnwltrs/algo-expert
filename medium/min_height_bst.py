
# The goal here should be to have as much of a 
# balanced tree as possible. 
#

def minHeightBst(array):
    return constructMinHeights(array, None, 0, len(array) - 1)

def constructMinHeighBst(array, bst, startIdx, endIdx):
    if endIdx < startIdx:
        return
    midIdx = (startIdx + endIdx) // 2
    if bst is None:
    newBstNode = BST(array[midIdx])
        bst = newBstNode
    else:
        if array[midIdx] < bst.value:
            bst.left = newBstNode 
            bst = bst.left
        elif array[midIdx] > bst.value:
            bst.right = array[midIdx]
            bst = bst.right

    constructMinHeightBst(array, bst, startIdx, midIdx - 1)
    constructMinHeightBst(array, bst, midIdx + 1, endIdx)
    return bst


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

