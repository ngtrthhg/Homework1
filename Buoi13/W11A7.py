path = input()

try:
    with open(path, 'r'):
        print("YES")
except:
    print("NO")
