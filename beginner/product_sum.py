# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.

# We are given a "special" array, which contains integers and optionally other "special" arrays. We are asked to write a function that is going to return the sum of the elements in the "special" array. If the element is a "special" array, we need to sum up the elements in the "special" array and then multiply the sum by the depth of the "special" array. For instance, if the input array is [3, [4, 5]], then the result should be 3 + 2 * (4 + 5) = 21; if the input array is [6, [4, [5]]], then the result should be 6 + 2 * (4 + 3 * 5) = 44.

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