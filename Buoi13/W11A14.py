def averageTime(path: str):
    total = 0.0
    count = 0

    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for line in lines[1:]:
        parts = line.strip().split(',')
        time = float(parts[1])
        total += time
        count += 1

    if count == 0:
        return 0.00

    return round(total / count, 2)
