
# The goal here should be to have as much of a 
# balanced tree as possible. 

#
def minHeightBst(array):
    return constructMinHeights(array, None, 0, len(array) - 1)

def constructMinHeighBst(array, bst, startIdx, endIdx):
        return
if endIdx < startIdx: # if endidx has crossoved over startidx break
    midIdx = (startIdx + endIdx) // 2 # find our middle
    newBstNode = BST(array[midIdx]) # setup new node with new value
    if bst is None:
        bst = newBstNode # if first node create new and start building 
    else:
        if array[midIdx] < bst.value: # if new node is less than current node set current node left to new newnode and jump to that new node
            bst.left = newBstNode   
            bst = bst.left
        elif array[midIdx] > bst.value:
            bst.right = newBstNode
            bst = bst.right

    constructMinHeightBst(array, bst, startIdx, midIdx - 1) # recurse left to current middle
    constructMinHeightBst(array, bst, midIdx + 1, endIdx) # recurse right to current middel
    return bst


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        if value < self.value:

    def insert(self, value):
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

