def runLengthEncoding(string):
    if string == " ":
        return "1 "
    
    output = []
    count = 1

    for idx in range(1, len(string)):
      
         if string[idx] == string[idx-1] and count != 9:
             count +=1
         else:
             output.append(count)
             output.append(string[idx-1])
             count = 1
             
         if idx == len(string)-1:
             output.append(count)
             output.append(string[idx])
    
    output = ''.join(map(str, output))
    return output