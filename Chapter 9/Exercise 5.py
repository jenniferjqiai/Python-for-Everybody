# This program records the domain name (instead of the address)
# where the message was sent from instead of who the mail came from (i.e., the whole email address).
# At the end of the program, print out the contents of your dictionary.

fname=input('Please enter a file name: ')
try:
    fhand=open(fname)
except:
    print('Cannot open file'+fname)
    exit()

count=dict()
for line in fhand:
    if line.startswith('From '):
        address = words = line.split()[1]
        domain=address.split('@')[1]
        count[domain]=count.get(domain,0)+1
print(count)