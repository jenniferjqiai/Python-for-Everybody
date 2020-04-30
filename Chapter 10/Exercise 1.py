# Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line.
# Count the num- ber of messages from each person using a dictionary.
# After all the data has been read,
# print the person with the most commits by creating a list of (count, email) tuples from the dictionary.
# Then sort the list in reverse order and print out the person who has the most commits.
fname=input('Enter the file name: ')
try:
    fhand=open(fname)
except:
    print(fname,'cannot be opened')
    exit()

count=dict()
for line in fhand:
    if line.startswith('From'):
        email = line.split()[1]
        count[email]=count.get(email,0)+1
print(count)
number = list()
for k,v in list(count.items()):
    number.append((v,k))
number.sort(reverse=True)
for key,val in number[0:1]:
    print(val,key)