# *args-  or variable-length arguments allow you to pass a variable number of arguments to a function.
def sum(*args):
    total = 0
    for num in args:
        total += num
    return total

result = sum(1,8, 2, 3, 15, 4, 5)
print(f"The sum of the numbers is: {result}")


# **key arguments-  or variable-length keyword arguments allow you to pass a variable number of keyword arguments to a function.
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name="Adil", age=25, city="New York")