fname=input('Enter a file name:')
try:
    fhand = open(fname)
except:
    print('File cannot be oppened :', fname)
    exit()
count=0
for line in fhand:
    count = count +1
print('There are', count,'subject lines in ',fname)