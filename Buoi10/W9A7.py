flowerbed = list(map(int, input().split()))
k = int(input())

n = len(flowerbed)
count = 0

for i in range(n):
    if flowerbed[i] == 0:
        if (i == 0 or flowerbed[i - 1] == 0) and (i == n - 1 or flowerbed[i + 1] == 0):
            flowerbed[i] = 1
            count += 1
            if count == k:
                break

if count == k:
    print("True")
else:
    print("False")
