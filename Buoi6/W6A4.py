s = list(map(str,input().split()))
d = {}
key = []
value = []
for i in range (len(s)):
  for j in range (len(s[i])):
    if s[i][j] == ":":
      key.append( s[i][:j] )
      value.append( s[i][j+1:])
for i in range (len(s)): d[key[i]] = []
for i in range (len(s)):
  d[key[i]].append(value[i])
print(d)