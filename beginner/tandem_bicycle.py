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