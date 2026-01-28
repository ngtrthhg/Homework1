try:
    N = int(input())
    if N <= 0:
        raise ValueError

    arr = list(map(int, input().split()))

    if len(arr) != N or any(x <= 0 for x in arr):
        raise ValueError

    if len(arr) != len(set(arr)):
        print("Mang khong hop le")
    else:
        print(sum(arr))

except ValueError:
    print("Mang khong hop le")
