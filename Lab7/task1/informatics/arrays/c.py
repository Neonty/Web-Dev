n = int(input())

a = list(map(int, input().split()))

cnt = sum(1 for x in a if x > 0)

print(cnt)