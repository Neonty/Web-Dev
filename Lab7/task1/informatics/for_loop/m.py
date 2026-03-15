n = int(input())

cnt = 0

for _ in range(n):
    number = int(input())
    if number == 0:
        cnt += 1
    
print(cnt)