def calculate_combination(n, r):
    if (r==0 or r==n):
        return 1
    return calculate_combination(n-1, r-1) + calculate_combination(n-1, r)
if __name__ == "__main__":

    n = int(input("enter the value of n:"))
    r = int(input("enter the value of r:"))
print(calculate_combination(n, r))