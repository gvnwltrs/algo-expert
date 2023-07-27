def nodeDepths(root):
    total_sum = [0] # use a list object to allow pass by reference
    depth_sums(root, 0, total_sum)
    print('Summing all of these depths yields {0}'.format(total_sum))
    return total_sum[0]

def depth_sums(node, depth, total_sum):
    if node is None:
        return

    current_depth = depth + 1
    print('The depth of the node with value {0} is {1}'.format(node.value, current_depth-1))
    total_sum[0] = total_sum[0] + (current_depth -1)
    if node.left is None and node.right is None:
        return 

    depth_sums(node.left, current_depth, total_sum)
    depth_sums(node.right, current_depth, total_sum)
        


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None