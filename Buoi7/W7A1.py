def binary_search(A, a):
    n = len(A)
    l = 0
    r = n - 1
    if a < A[l] or a > A[r]: return -1
    while l <= r:
        mid = (l + r) // 2
        if A[mid] == a: return mid
        elif A[mid] < a : l = mid + 1
        else : r = mid - 1
    return -1

A = list(map(int,input().split()))
a = int(input())
print( binary_search(A,a))