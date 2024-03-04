import math
 
def primeCheck(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

print(primeCheck(20)) # False
print(primeCheck(85)) # False
print(primeCheck(3)) # True