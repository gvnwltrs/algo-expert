def commonCharacters(strings):
    STRINGS_COUNT = len(strings)-1
    count = 0 
    common_char = set()
    for char in strings[0]:
        for string in range(1, len(strings)):
            if char in strings[string]:
                count += 1
        if count == STRINGS_COUNT:
            common_char.add(char)
        count = 0
    return common_char
