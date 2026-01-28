def count(path: str, character: str) -> int:
    with open(path, 'r') as f:
        sentence = f.read()
    return sentence.count(character)
