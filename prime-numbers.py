from math import sqrt

def isPrime(num):
    if num < 1:
        return False
    elif num <=2:
        return True
    else:
        for i in range(2, int(sqrt(num)) +1):
            if num % i == 0:
                return False
    return True

'''Manual Tests'''

print(isPrime(7))
print(isPrime(21))
print(isPrime(49))
print(isPrime(3))
print(isPrime(9))
print(isPrime(11))
print(isPrime(15))


