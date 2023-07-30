
# s1
def threeNumberSum(array, targetSum):
    triplets = []

    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            for k in range(j+1, len(array)):
                if array[i] + array[j] + array[k] == targetSum:
                    temp = [array[i], array[j], array[k]]
                    temp.sort()
                    triplets.append(temp)
    triplets.sort()
    return triplets

