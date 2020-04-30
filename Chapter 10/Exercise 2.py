#  This program counts the distribution of the hour of the day for each of the messages.
#  You can pull the hour from the “From” line by finding the time string and then splitting that string into
#  parts using the colon character.
#  Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.
import string

fname=input('Enter the file name: ')
try:
    fhand=open(fname)
except:
    print(fname,'cannot be opened')
    exit()

count=dict()
time=list()
for line in fhand:
    if line.startswith('From '):
        line = line.split()
        time=line[5]
        hour=time.split(':')[0]
        count[hour] = count.get(hour, 0) + 1
lst=list()
for h,t in (count.items()):
    lst.append((h,t))
lst.sort()
for i in lst:
    print(i[0],i[1])
