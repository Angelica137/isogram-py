def isogram(word: str) -> bool:
    for i in range(len(word) - 1):
        j = i + 1
        if word[i] == word[j] and word[i] != " " and word[i] != "-":
            return False
    return True
