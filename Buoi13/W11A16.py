import math

path = input().strip()

with open(path, 'r', encoding='utf-8') as f:
    lines = [line.strip() for line in f.readlines() if line.strip() != ""]

i = 0
while i < len(lines):
    shape_type = lines[i].split(":")[1].strip()
    params = lines[i + 1]

    if shape_type == "SQUARE":
        side = float(params.split(":")[1])
        perimeter = 4 * side

    elif shape_type == "RECTANGLE":
        parts = params.split()
        width = float(parts[1])
        height = float(parts[3])
        perimeter = 2 * (width + height)

    elif shape_type == "CIRCLE":
        radius = float(params.split(":")[1])
        perimeter = 2 * math.pi * radius

    else:
        i += 2
        continue

    print(f"{perimeter:.2f}")
    i += 2
