<<<<<<< HEAD
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
=======
fname = "mbox-short.txt"
hand = open(fname)
#..
lst = list()

for line in hand:
    if not line.startswith("From:"): continue
    line = line.split()
    lst.append(line[1])

counts = dict()
for word in lst:
    counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.items(): 
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word

print (bigword,bigcount)
>>>>>>> 72723d959fa9a9b63fb19561da7157aacff78736
