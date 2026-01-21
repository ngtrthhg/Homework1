def is_subarray(list1, list2):
    n = len(list1)
    for i in range(len(list2) - n + 1):
        if list2[i:i+n] == list1:
            return "YES"
    return "NO"

a = list(map(int,input().split()))
b = list(map(int,input().split()))
print(is_subarray(a, b))