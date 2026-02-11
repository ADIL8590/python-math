# *args-  or variable-length arguments allow you to pass a variable number of arguments to a function.
def sum(*args):
    total = 0
    for num in args:
        total += num
    return total

result = sum(1,8, 2, 3, 15, 4, 5)
print(f"The sum of the numbers is: {result}")