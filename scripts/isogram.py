def isogram(word: str) -> bool:
    chars = [char.lower() for char in word if char.isalpha()]
    return len(chars) == len(set(chars))
