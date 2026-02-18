# Checking if a number is prime using recursion code1

def is_prime(n, i=2):
    if (n<=2):
        return True if n==2 else False
    if (n%i==0):
        return False
    if (i*i>n):
        return True
    return is_prime(n, i+1)
print(is_prime(29))
# Checking if a number is prime using recursion code2
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
print(is_prime(23))


