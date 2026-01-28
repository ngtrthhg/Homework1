def countCharacter(path: str, letter: str) -> int:
    with open(path, 'r') as f:
        text = f.read().lower()
    return text.count(letter.lower())
