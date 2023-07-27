def generateDocument(characters, document):
    if len(document) == 0:
        return True

    matched = []
    characters_tokenized = [char for char in characters]
    for doc_char in document:
        for char in characters_tokenized:
            if doc_char == char:
                matched.append(doc_char) 
                characters_tokenized.remove(char)
                break
    matched = ''.join(matched)
    if matched == document:
        return True
    return False