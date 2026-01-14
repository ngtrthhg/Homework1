def check(A , k):
    for i in range (len(A)):
        for j in range (i, len(A)):
            if A[i] == A[j] and  j - i <= k: return True
    return False
    

A = input().split()
k = int(input())
print(check(A, k))
