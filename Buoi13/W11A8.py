n = int(input())

a = "a"
b = "b"

with open("output.txt", "w", encoding="utf-8") as f:
    if n >= 0:
        f.write(a + "\n")
    if n >= 1:
        f.write(b + "\n")

    for _ in range(2, n + 1):
        a, b = b, b + a
        f.write(b + "\n")
