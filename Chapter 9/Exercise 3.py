# Write a program to read through a mail log,
# build a his- togram using a dictionary to count how many messages have come from each email address,
# and print the dictionary.

fname=input('Please enter a file name: ')
try:
    fhand=open(fname)
except:
    print('Cannot open file'+fname)
    exit()

count=dict()
email=[]
for line in fhand:
    words = line.split()
    if len(words)  == 0 :continue
    if words[0] != 'From' : continue
    address=words[1]
    email.append(address)
for n in email:
    if n not in count:
        count[n] = 1
    else:
        count[n] += 1
print(count)