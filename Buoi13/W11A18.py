import math

def estimatedTime(path: str):
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    src = lines[0].split()
    x1 = float(src[2])
    y1 = float(src[4])

    des = lines[1].split()
    x2 = float(des[2])
    y2 = float(des[4])

    velocity = float(lines[2].split()[1])

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    time = distance / velocity

    return round(time, 2)
