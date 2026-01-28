path = input().strip()

try:
    with open(path, 'r', encoding='utf-8') as f:
        data = f.read().split()

    numbers = list(map(int, data))

    print(max(numbers), min(numbers))

except:
    print("Mission failed")
