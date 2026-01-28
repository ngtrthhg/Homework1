def getMoney(path: str) -> list[int]:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read().strip()

    if content == "":
        return []

    return list(map(int, content.split()))


def rob(houses: list[int]) -> int:
    if not houses:
        return 0

    if len(houses) == 1:
        return houses[0]

    prev2 = houses[0]
    prev1 = max(houses[0], houses[1])

    for i in range(2, len(houses)):
        current = max(prev1, prev2 + houses[i])
        prev2 = prev1
        prev1 = current

    return prev1


path = input().strip()

houses = getMoney(path)
max_money = rob(houses)

print(max_money)
