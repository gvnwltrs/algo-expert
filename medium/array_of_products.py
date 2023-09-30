


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
