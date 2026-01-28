def areAnagrams(path1: str, path2: str) -> bool:
    with open(path1, 'r') as f1:
        s1 = f1.read().lower()
    with open(path2, 'r') as f2:
        s2 = f2.read().lower()

    s1 = ''.join(c for c in s1 if c.isalpha())
    s2 = ''.join(c for c in s2 if c.isalpha())

    return sorted(s1) == sorted(s2)
