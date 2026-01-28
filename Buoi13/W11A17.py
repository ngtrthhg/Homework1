def productExceptSelf(path: str) -> list[int]:
    with open(path, 'r', encoding='utf-8') as f:
        data = list(map(int, f.read().split()))

    n = len(data)
    result = [1] * n

    left = 1
    for i in range(n):
        result[i] = left
        left *= data[i]

    right = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right
        right *= data[i]

    return result
