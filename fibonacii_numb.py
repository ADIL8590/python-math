#Fibonacci number in fib-sequence using recursion code1
def fibonacci(n):
    if (n==0):
        return 0
    if (n==1):
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(7))

#Alternative code2 of Fibonacci sequence using iteration
def fibonacci_iter(n):
    fib_seq = []
    a, b = 0, 1
    for _ in range(n):
        fib_seq.append(a)
        a, b = b, a + b
    return fib_seq
print(fibonacci_iter(7))

#Alternative code3 of Fibonacci sequence using if else
def fibonacci_ifelse(n):
    if n<=0:
        return []
    elif n==1:
        return [0]
    elif n==2:
        return [0,1]
    else:
        fib_seq = [0,1]
        for i in range(2,n):
            next_fib = fib_seq[i-1] + fib_seq[i-2]
            fib_seq.append(next_fib)
        return fib_seq
print (fibonacci_ifelse(7))
#Fibonacci number in fib-sequence using memoization code4
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        memo[n] = fibonacci_memo(n-1,memo) + fibonacci_memo(n-2,memo)
        return memo[n]
print(fibonacci_memo(7))