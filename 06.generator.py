#!/usr/bin/python3

def isprime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

# this is the generator
def primes(n = 1):
   while(True):
       if isprime(n): yield n # yield is like return but continues
       n += 1 

for n in primes():
    if n > 100: break
    print(n)

