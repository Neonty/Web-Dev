b = input()
d = 0
num = 0
for i in range(len(b)-1,-1,-1):
    num += int(b[i]) * 2**d
    d += 1

print(num)