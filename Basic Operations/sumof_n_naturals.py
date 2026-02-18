#calculate sum of first n-natural numbers using recursion
n=int(input("Enter a number n to calculate sum of first n natural numbers: ")) #taking input from user
def cal_sum(n):  #function to calculate sum using recursion
    if (n==0):   #base case
        return 0 #if n=0 , sum=0
    return cal_sum(n-1)+n    #recursive case: sum of first n numbers = sum of first (n-1) numbers + n
    

print(f"The sum of numbers from 1 to {n} is: {cal_sum(n)}")  #printing the sum , say user input is 50, output will be "The sum of numbers from 1 to 50 is: 1275"



# finding sum of first n natural numbers using for loop
n=int(input("Enter a number n to calculate sum of first n natural numbers: "))  #taking input from user 
sum=0       #initializing sum variable
for i in range(1,n+1):   #loop from 1 to n
    sum=sum+i            #adding each number to sum
print(f"The sum of numbers from 1 to {n} is: {sum}")    #printing the sum , say user input is 50, output will be "The sum of numbers from 1 to 50 is: 1275"

