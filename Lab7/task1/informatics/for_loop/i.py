x = int(input())

divisors = 0

for i in range(1, int(x**0.5)+1):
    if x % i == 0:
        divisors += 2
        if i * i == x:
            divisors -= 1

print(divisors)