#Erostehesis prime length
def erostephene_prime(n):
    primes = [True for i in range(n+1)]
    p = 2
    while (p*p <= n):
<<<<<<< HEAD
        if (primes[p] ):
=======
        if (primes[p]):
>>>>>>> 5e73dff169acf771524f7056655ecfa992c5c6d8
            for i in range(p*p, n+1, p):
                primes[i] = False
        p += 1
    prime_numbers = []
    for p in range(2, n):
        if primes[p]:
            prime_numbers.append(p)
    return prime_numbers
print(erostephene_prime(30))
