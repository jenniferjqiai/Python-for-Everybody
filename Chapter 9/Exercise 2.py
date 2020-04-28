# Write a program that categorizes each mail message by which day of the week the commit was done.
# To do this look for lines that start with “From”,
# then look for the third word and keep a running count of each of the days of the week.
# At the end of the program print out the contents of your dictionary (order does not matter).
fname=input('Please enter a file name: ')
try:
    fhand=open(fname)
except:
    print('Cannot open file'+fname)
    exit()

count=dict()
dates=[]
for line in fhand:
    words = line.split()
    if len(words)  == 0 :continue
    if words[0] != 'From' : continue
    date=words[2]
    dates.append(date)
for n in dates:
    if n not in count:
        count[n] = 1
    else:
        count[n] += 1
print(count)