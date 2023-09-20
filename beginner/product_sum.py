# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array):
    start_depth = 1
    sum = depth_sum(array, start_depth)
    return sum 

def depth_sum(array, depth):
    sum = 0
    for elem in array:
        if type(elem) is list:
            sum += depth_sum(elem, depth+1)
        else:
            sum += elem
      
    return sum * depth