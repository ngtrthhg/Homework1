def moveZeroes(fileName: str) -> list:
    with open(fileName, 'r', encoding='utf-8') as f:
        n = int(f.readline().strip())
        arr = list(map(int, f.readline().split()))

    result = []
    zero_count = 0

    for x in arr:
        if x == 0:
            zero_count += 1
        else:
            result.append(x)

    result.extend([0] * zero_count)
    return result
