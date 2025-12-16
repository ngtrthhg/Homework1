A = tuple(map(int,input().split()))
odd = []
even = []
for i in A:
  if i % 2 == 0: even.append(i)
  else : odd.append(i)
print(tuple(even))
print(tuple(odd))