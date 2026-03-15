x = input()

num = 0

for i in range(len(x)-1,-1,-1):
    num = num*10+int(x[i])
print(num)