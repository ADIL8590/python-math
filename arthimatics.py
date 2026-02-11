def arthimatics(a,b):
    sum = a + b
    difference = a - b
    product = a * b
    quotient = a / b if b != 0 else "undefined"
    
    return sum, difference, product, quotient
# Get user input for two numbers
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
# Perform arthimatics operations
sum_result, difference_result, product_result, quotient_result = arthimatics(a, b)
print(f"Sum of {a} and {b}: {sum_result}")
print(f"Difference of {a} and {b}: {difference_result}")
print(f"Product of {a} and {b}: {product_result}")
print(f"Quotient of {a} and {b}: {quotient_resultm}")