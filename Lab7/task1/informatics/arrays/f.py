n = int(input())

a = list(map(int, input().split()))
localPeaks = 0

for i in range(1, n - 1):
    if a[i] > a[i - 1] and a[i] > a[i + 1]:
        localPeaks += 1

print(localPeaks)