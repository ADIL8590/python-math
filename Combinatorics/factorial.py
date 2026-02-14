#finding factorial of a number using recursion by user input
n=int(input("Enter a number: "))
def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        return  fact(n-1)*n
print(f"Factorial of {n} is {fact(n)}")
# Finding factorial of a number using loop by user input
n=int(input("Enter a number to find its factorial: "))
factorial = 1
for i in range(1, n+1):
    factorial *= i
print(f"The factorial of {n} is: {factorial}")
