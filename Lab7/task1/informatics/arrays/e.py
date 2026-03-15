n = int(input())

a = list(map(int, input().split()))
hasSameSign = False

for i in range(1, n):
    if a[i] * a[i-1] > 0:
        hasSameSign = True
        break

print("YES" if hasSameSign else "NO")