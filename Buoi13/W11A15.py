def findMovies(path: str):
    result = []

    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for line in lines[1:]:
        parts = [p.strip() for p in line.split(',')]

        movie = parts[1]
        description = parts[2].lower()
        rating = float(parts[3])

        if rating > 8.0 and description != "boring":
            result.append(movie)

    if not result:
        return "All are boring!"

    return result
