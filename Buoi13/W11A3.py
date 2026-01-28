def housesOfHogwarts(path: str):
    with open(path, 'r') as f:
        lines = f.read().splitlines()

    n = int(lines[0])
    names = lines[1:]

    for name in names:
        print(name)
