
# Given a non-empty string, we are asked to write a function that is going to run-length-encode the input string and return the encoded string. Run-length encoding refers to replacing repetitive, consecutive data by a count and one copy of a repeated data. For instance, AAABB will be encoded as 3A2B. If a sequence contains more than 9 consecutive, identical characters, we first encode 9 characters, then the remaining ones. For instance, AAAAAAAAAA (10 As) will be encode as 9A1A.

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