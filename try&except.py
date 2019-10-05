#try and except:conditional statements

N1=input("Enter number 1:")
N2=input("Enter number 2:")
N3=input("Enter number 3:")
a=float(N1)
b=float(N2)
c=float(N3)
try:
    x=(a*b)/c
    print(x)
except:
    y=(b*c)/a
    print(y)
input(".")
