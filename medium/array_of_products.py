
'''
Write a function that takes in a non-empty array of integers and returns an array of the same size, where each element in the
output array is equal to the product of every other number in the input array. 

In other words, output[i] is equal to the product every number in the input array other than input[i]. 
'''

def arrayOfProducts(array):
    output = []

    for i in range(len(array)):
        cursor = 0
        end = len(array)-1
        product = 1
        while cursor <= end:
            if cursor == i:
                cursor += 1
                continue
            if array[cursor] == 0:
                product = 0
                break
            product *= array[cursor]
            cursor += 1
        output.append(product)
            
    
    return output
