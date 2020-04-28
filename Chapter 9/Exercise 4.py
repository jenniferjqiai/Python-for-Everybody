# Add code to the above program to figure out who has the most messages in the file.
# After all the data has been read and the dic- tionary has been created,
# look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops)
# to find who has the most messages and print how many messages the person has.
fname=input('Please enter a file name: ')
try:
    fhand=open(fname)
except:
    print('Cannot open file'+fname)
    exit()

count=dict()
email=list()
for line in fhand:
    words = line.split()
    if len(words)  == 0 :continue
    if words[0] != 'From' : continue
    address=words[1]
    email.append(address)
#print(email)
for n in email:
    if n not in count:
        count[n] = 1
    else:
        count[n] += 1
value=list(count.values())
key=list(count.keys())
Maximun=max(value)
print(key[value.index(Maximun)], Maximun)

