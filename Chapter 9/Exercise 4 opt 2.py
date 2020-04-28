fname=input('Please enter a file name: ')
try:
    fhand=open(fname)
except:
    print('Cannot open file'+fname)
    exit()
di=dict()
e=list()
for line in fhand:
    w = line.split()
    if len(w) == 0 :continue
    if w[0] != 'From' : continue
    k=w[1]
    e.append(k)
# print(e)
for address in e:
    if address in di:
        di[address] = di[address] +1
    else:
        di[address] = 1
print(di)
largest=-1
theemail = None
for key,value in di.items():
    if value > largest:
        largest = value
        theemail=key
print(theemail,largest)
