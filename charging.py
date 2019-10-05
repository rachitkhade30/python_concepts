#code: charging $10.5/hr for first 40 hours. Charging 1.5 times for the subsequent hours
#functions, parameters to function, return function, conditional statements
def compute(h,r):
    if h<40:
        l=h*r
        return (l)
    else:
        x=h-40
        b=((r*40)+(x*1.5*r))
        return(b)
hour=input("Enter Total Hours:")
rate=input("Enter rate/hr:")
h=float(hour)
r=float(rate)
pay=compute(h,r)
print("You have to pay","$",pay)
input(".")
