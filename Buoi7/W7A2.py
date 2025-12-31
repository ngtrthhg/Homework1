import bisect

def count_occurences(A, a):
    A.sort()
    lb = bisect.bisect_left(A, a) 
    ub = bisect.bisect_right(A, a)
    return ub - lb 

A  = list(map(int,input().split()))
a = int(input())
print(count_occurences(A, a))