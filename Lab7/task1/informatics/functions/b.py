def bin_power(a, b):
    result = 1.0
    while(b>0):
        if (b & 1):
            result = result * a
        a = a * a
        b >>= 1
    
    return result

a, b = input().split()
print(bin_power(float(a), int(b)))