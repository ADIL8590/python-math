# Code to generate all permutations of a list of elements
def generate_permutations(elements):   # This code generates all permutations
    if len(elements) == 0:           # edge case: empty list
        return [[]]           # base case: single permutation of empty list is a list with an empty list
    
    perms = []                 # list to store all permutations
    for i in range(len(elements)):   # iterate through each element
        current = elements[i]        # select the current element
        remaining = elements[:i] + elements[i+1:]    # get the remaining elements
        for p in generate_permutations(remaining):  # recursively generate permutations of remaining elements
            perms.append([current] + p)       # append current element to each permutation of remaining elements
    
    return perms
# Example usage
if __name__ == "__main__":   
    elements = [1, 2, 3]
    permutations = generate_permutations(elements)    # generates  all permutation elements 
    for perm in permutations:
        print(perm)                                            # return the list of permutations
    print(f"Total permutations of {len(elements)} elements: {len(permutations)}")                       #Total number of permutations
      # This code generates all permutations  taking a list of 3 elements as input.

#  code for permuting r elements from n elements (General formullacode for counting number of permutations, above resulted will be output if r=n)
def generate_permutations_r(elements, r):  # This code generates all permutations of r elements from the list of elements
    if r == 0:                             # edge case: permutation of length 0
        return [[]]                        # base case: single permutation of length 0 is a list with an empty list
    if len(elements) < r:                  # edge case: not enough elements to permute
        return []                          # no permutations possible
    
    perms = []                              # list to store all permutations
    for i in range(len(elements)):          # iterate through each element
        current = elements[i]               # select the current element
        remaining = elements[:i] + elements[i+1:]  # get the remaining elements
        for p in generate_permutations_r(remaining, r - 1):  # recursively generate permutations of remaining elements with r-1
            perms.append([current] + p)     # append current element to each permutation of remaining elements
    
    return perms                          # return the list of permutations
# Example usage
if __name__ == "__main__":              #calling the function to generate permutations of r elements
    elements = [1, 2, 3, 4]             # list of elements
    r = 2                               # number of elements to permute
    permutations_r = generate_permutations_r(elements, r)      # generate permutations of r elements
    for perm in permutations_r:                                # console output
        print(perm)      # This code generates all permutations of r elements from the list of elements.
# print the total number of and permutation
    print(f"Total permutations of {r} elements from {len(elements)} elements i.e : {len(permutations_r)}")


""" using the formula P(n,r) = C(n,r) * r! to calculate permutation. I will reuse the factorial and combination functions from the previous snippets."""

def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        return  fact(n-1)*n
def calculate_combination(n, r):
    if (r==0 or r==n):
        return 1
    return calculate_combination(n-1, r-1) + calculate_combination(n-1, r)
def calculate_permutation(n, r):
    return calculate_combination(n, r) * fact(r)
if __name__ == "__main__":
    n = int(input("Enter the value of n: "))
    r = int(input("Enter the value of r: "))
    # This code calculates the number of combinations of r elements from n elements 
    print(f"Total combinations C({n},{r}) is: {calculate_combination(n, r)}")
    #This code calculates the number of permutations of r elements from n elements using the formula P(n,r) = C(n,r) * r!
    print(f"Total permutations P({n},{r}) is: {calculate_permutation(n, r)}")

# This code calculates the number of permutations of r elements from n elements using the formula P(n,r) = n! / (n-r)!
def calculate_permutation_formula(n, r):
    return fact(n) // fact(n - r)
if __name__ == "__main__":
    n = int(input("Enter the value of n: "))
    r = int(input("Enter the value of r: "))
    # This code calculates the number of permutations of r elements from n elements using the formula P(n,r) = n! / (n-r)!
    print(f"Total permutations P({n},{r}) using formula is: {calculate_permutation_formula(n, r)}")
    
    
    

