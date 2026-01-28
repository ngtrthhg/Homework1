lst = input().split()
result = []

for x in lst:
    try:
        result.append(int(x))
    except ValueError:
        print(f"Cảnh báo: không thể chuyển {x} sang int")

print(result)
