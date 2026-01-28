def imageSmoother(path: str):
    with open(path, 'r', encoding='utf-8') as f:
        M = int(f.readline().strip())
        img = [list(map(int, f.readline().split())) for _ in range(M)]

    result = [[0] * M for _ in range(M)]

    for i in range(M):
        for j in range(M):
            total = 0
            count = 0

            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if 0 <= x < M and 0 <= y < M:
                        total += img[x][y]
                        count += 1

            result[i][j] = total // count

    for row in result:
        print(*row)
