a, b = map(int,input().split())
try:
    print("{:.2f}".format(a/b))
except ZeroDivisionError:
    print("Loi chia khong")