# Conditional Execution

hrs = float(input("Enter hours worked: "))
rate=float(input("Enter rate per hour: "))
if hrs>40:
    print(((hrs-40)*(rate*1.5))+(40*rate))
else:
    print(hrs*rate)