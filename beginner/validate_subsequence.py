#!/urs/bin/env python3


def isValidSubsequence(array, sequence):
    # Write your code here.
    list_check = []
    last = None
    
    for i in range(len(array)):
        for j in range(len(sequence)):
            # last = sequence[i]
            if array[i] == sequence[j] and len(list_check) < len(sequence) and sequence[j] != last:
                list_check.append(sequence[j])
                last = sequence[j]
            else:
                last = None
                
    print('seqence: ', sequence, 'check: ',  list_check)
      
    if sequence == list_check:
        return True
    else:
        return False