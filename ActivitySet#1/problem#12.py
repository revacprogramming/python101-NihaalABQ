"""10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below."""


file = input("Enter the file name: ")
fh = open(file,'r')
details = {}
for l in fh:
    if l.startswith("From "):
        time = l.split()[5]
        hr = time.split(":")[0]
        details[hr] = details.get(hr,0)+1
lst = list(details.items())
lst.sort()
print(lst)
"""for t in lst:
    print(t[0], t[1])"""