def isogram(word: str) -> bool:
    chars = {}
    for i in range(len(word)):
        if word[i] in chars and word[i] != " " and word[i] != "-":
            return False
        else:
            chars[word[i].lower()] = 1
    return True
