def longestPeak(array):
    longest_peak = 0
    
    for i in range(1, len(array)-1):
        if array[i-1] < array[i] and array[i] > array[i+1]:
            left = 1
            right = 0
            l = i-1
            while l >= 0 and array[l] < array[l+1] :
                left += 1 
                l -= 1
            r = i+1
            while r <= len(array)-1 and array[r] < array[r-1]:
                right += 1
                r += 1
            total = left + right
            longest_peak = total if total > longest_peak else longest_peak
    
    return longest_peak