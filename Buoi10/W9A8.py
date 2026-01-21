def is_path_crossing(moves):
    x, y = 0, 0
    visited = set()
    visited.add((0, 0))

    for move in moves:
        if move == 'R': x += 1
        elif move == 'L': x -= 1
        elif move == 'U': y += 1
        elif move == 'D': y -= 1
        if (x, y) in visited:
            return True
        visited.add((x, y))
    return False

moves = input()
print(is_path_crossing(moves))