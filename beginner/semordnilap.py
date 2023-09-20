def semordnilap(words):
    semordnilaps = []
    reversed_words = [word[::-1] for word in words]

    for i in range(len(words)-1):
        for j in range(i+1, len(reversed_words)):
            if words[i] == reversed_words[j]:
                semordnilaps.append([words[i], words[j]])
                break
        
    return semordnilaps

