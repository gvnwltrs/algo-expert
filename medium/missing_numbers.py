def missingNumbers(nums):
    compare_list = [i+1 for i in range(len(nums)+2)]
    output = list(filter(lambda x: x not in nums, compare_list))
    return output