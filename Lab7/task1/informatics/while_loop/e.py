n = int(input())

i = 0
power = 1

while i <= n:
    if power >= n:
        print(i)
        break
    power *= 2
    i += 1