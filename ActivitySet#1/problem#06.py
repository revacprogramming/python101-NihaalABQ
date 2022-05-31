# Loops & Iterators

largest = 0
smallest = 0

while True:
    num = input("Enter a number? ")

    if num == "done":
        break

    try:
        n=int(num)
    except:
        print("Invalid input")
        continue
    if largest is 0:
        largest=n
    if smallest is 0:
        smallest=n
    if largest < n:
        largest=n
    if smallest > n:
        smallest=n
print("Maximum is", largest)
print("Minimum is",smallest)