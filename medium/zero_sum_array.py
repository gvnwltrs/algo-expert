def zeroSumSubarray(nums):
    print('nums length:', len(nums))
    if len(nums) == 0: 
        return False
    elif len(nums) == 1:
        return True if nums[0] == 0 else False

    if sum(nums) == 0:
        return True

    print(nums[2])
    l = 0 
    r = 1 
    sums = nums[0]
    while l < len(nums)-1:
        if sums == 0 or nums[r] == 0:
            return True
        elif r <= len(nums)-1:
            print('index r at: ', r)
            sums += nums[r]
            if sums == 0:
                return True
            r += 1
            
        if r > len(nums)-1:
            l += 1
            r = l + 1
            sums = nums[l]
   
    return False