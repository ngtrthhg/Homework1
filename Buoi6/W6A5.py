A = list(map(int,input().split()))
d ={}
d['positives'] = 0
d['negatives'] = 0
d['zeros'] = 0
for i in A:
  if i > 0: d['positives'] += 1
  elif i < 0: d['negatives'] += 1
  else : d['zeros'] += 1
print(d)