import struct

path = input().strip()

with open(path, 'rb') as f:
    while True:
        data = f.read(8) 
        if not data:
            break

        number = struct.unpack('d', data)[0]
        print(f"{number:.5f}")
