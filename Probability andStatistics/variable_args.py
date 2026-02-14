# *args-  or variable-length arguments allow you to pass a variable number of arguments to a function.
"""def sum(*args):
    total = 0
    for num in args:
        total += num
    return total

result = sum(1,8, 2, 3, 15, 4, 5)
print(f"The sum of the numbers is: {result}")"""


# **key arguments-  or variable-length keyword arguments allow you to pass a variable number of keyword arguments to a function.
def print_info(School,Name,Parentage,ID,Class,Session,**kwargs):
    percentage=sum(kwargs.values())/len(kwargs)
    print(f"School: {School}")
    print(f"Name: {Name}")
    print(f"Parentage: {Parentage}")
    print(f"ID: {ID}")
    print(f"Class: {Class}")
    print(f"Session: {Session}")
    print(f"Percentage: {percentage}%")
    for key, value in kwargs.items():
        print(f"Marks obetained in {key}: is {value}")
    
print_info(School="CHILD CARE School WAVOORA LOLAB", Name="SHAH QURAT UL EIN", Parentage="ADIL MUKHTAR", ID=12345, Class="Ist", Session="2026", Maths=100, English=99, Science=98, Social_Studies=97, Computer_Science=96)