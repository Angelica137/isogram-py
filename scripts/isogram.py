def isogram(word: str) -> bool:
    for i in range(len(word) - 1):
        j = i + 1
        while j <= len(word) - 1:
            if word[i] == word[j] and word[i] != " " and word[i] != "-":
                return False
            else:
                j += 1
    return True
