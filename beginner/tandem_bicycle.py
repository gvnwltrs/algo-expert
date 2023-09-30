
# We are given two arrays of positive integers: the first one represents the speeds of riders with red shirts and the second one represents the speeds of riders with blue shirt. Both array have the same length. We will also receive a Boolean fastest.

# We are asked to write a function that is going to pair every red-shirt rider with a blue-shirt rider to operate a tandem bicycle. A tandem bicycle is a bicycle operated by two people. The speed of the bicycle is dictated by the rider who pedals faster, for instance, if the speed of one rider is 5 and the speed of the other rider is 3, then the speed of the bicycle is 5. If the Boolean fastest is true, the function should return the total maximum speed of all tandem bicycles being ridden; otherwise return the total minimum speed.

# Example 1:

# Input:
# redShirtSpeeds = [3, 9, 2]
# blueShirtSpeeds = [7, 2, 1]
# fastest = true

# Output: 19
# Example 2:

# Input:
# redShirtSpeeds = [3, 9, 2]
# blueShirtSpeeds = [7, 2, 1]
# fastest = false

# Output: 14

def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    sum = 0
    redShirtSpeeds.sort()
    if fastest:
        blueShirtSpeeds.sort(reverse=True)
    else: 
        blueShirtSpeeds.sort()
        
    for r_index, r_value in enumerate(redShirtSpeeds):
         # check.append(max(r_value, blueShirtSpeeds[r_index]))
        sum += max(r_value, blueShirtSpeeds[r_index])
                
    return sum