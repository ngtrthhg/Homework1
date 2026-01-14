def unique_sorted_student_ids(a, b):
    s = set()
    for x in a + b:
        s.add(int(x))
    return [str(x) for x in sorted(s)]

a = input().split()
b = input().split()

result = unique_sorted_student_ids(a, b)

print(result)
