def isogram(word: str) -> bool:
    chars = {}
    for i in range(len(word)):
        if word[i] in chars and word[i] != " " and word[i] != "-":
            print(i)
            return False
        else:
            chars[word[i]] = 1
    return True
    for i in range(len(word)):
        j = i + 1
        while j <= len(word) - 1:
            if word[i] == word[j] and word[i] != " " and word[i] != "-":
                return False
            else:
                j += 1
    return True


print(isogram("eleven"))
