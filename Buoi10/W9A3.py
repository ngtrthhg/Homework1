def smallest_after_one_swap(n):
    n = list(n)
    length = len(n)
    for i in range(length):
        min_digit = n[i]
        pos = -1
        for j in range(i + 1, length):
            if min_digit > n[j] :
                pos = j
                min_digit = n[j]
        if pos != -1:
            n[i], n[pos] = n[pos], n[i]
            return n
        
    n[length - 2], n[length - 1] = n[length - 1], n[length - 2]
    return n

n = input()
n = smallest_after_one_swap(n)
while n[0] == '0': n = n[1:]
print("".join(n))

