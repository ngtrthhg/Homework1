import math

try:
    x = float(input())
    if x < 0:
        raise ValueError
    print(f"{math.sqrt(x):.2f}")

except ValueError:
    print("So am")
