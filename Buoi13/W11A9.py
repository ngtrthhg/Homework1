def grade10(path: str):
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for line in lines[1:]:
        parts = line.strip().split(',')

        ho = parts[1]
        ten = parts[2]
        thcs4 = parts[5]

        if thcs4 == '10':
            print(ho + " " + ten)
