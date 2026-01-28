def canWinNim(path: str) -> bool:
    with open(path, 'r') as f:
        n = int(f.read().strip())
    return n % 4 != 0
