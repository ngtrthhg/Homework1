def reverse(path: str) -> int:
    with open(path, 'r') as f:
        n = f.read().strip()
    return int(n[::-1])
