# Functions


def computepay(h, r):
    if h>40:
        pay=(((h-40)*(r*1.5))+(40*r))
    else:
        pay=(h*r)
    return pay    


hrs = float(input("Enter hours? "))
rte = float(input("Enter rate per hour? "))

p = computepay(hrs, rte)
print("Pay", p)
