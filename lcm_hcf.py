def hcf(a,b):
    if b==0:
        return a
    else:
        return hcf(b,a%b)
print (hcf(50,15))
def lcm(a,b):
        return (a*b)//hcf(a,b)
print (lcm(50,15))