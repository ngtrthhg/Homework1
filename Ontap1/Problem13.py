def balanced_array(n):
    if n % 2 != 0:
        return ('NO', [])
    k = n // 2
    if k % 2 != 0:
        return ('NO', [])
    even = []
    odd = []
    for i in range(1, k + 1):
        even.append(2 * i)
    total_even = sum(even)
    for i in range(1, k):
        odd.append(2 * i - 1)
    total_odd = sum(odd)
    odd.append(total_even - total_odd)
    return ('YES', even + odd)

n =int(input())
print(balanced_array(n))
