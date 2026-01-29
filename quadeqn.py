def cal_roots_poly(a,b,c):
    a= int(a)
    b= int(b)
    c= int(c)
    dis= (b**2-4*a*c)
    if dis>0:
        root1= (-b + dis**0.5)/(2*a)
        root2= (-b - dis**0.5)/(2*a)
        print("Roots are real and distinct:", root1, root2)
    elif dis==0:
        root= -b/(2*a)
        print("Roots are real and equal:", root)
    else:
        real_part= -b/(2*a)
        imag_part= (-dis**0.5)/(2*a)
        print("Roots are complex:", complex(real_part, imag_part), complex(real_part, -imag_part))
# Example usage
cal_roots_poly(1,-3,2)