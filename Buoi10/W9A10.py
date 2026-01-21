import bisect

def findRadius(A, B):
    B.sort()
    ans = 0
    for i in range (len(A)):
        if A[i] <= B[0]: ans = max(ans, B[0] - A[i])
        elif A[i] > B[len(B) - 1]: ans = max(ans, A[i] - B[len(B) - 1])
        else:
            x = bisect.bisect_left(B, A[i])
            ans = max(min(abs(B[x] - A[i]), abs(B[x - 1] - A[i])), ans)

    return ans    
    
A = list(map(int,input().split()))
B = list(map(int,input().split()))
print(findRadius(A, B))

