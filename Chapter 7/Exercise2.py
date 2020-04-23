filename=input('Enter a file name:')
faut=open(filename)
count=0
sum = 0.0
length=len('X-DSPAM-Confidence:')
for line in faut:
    if line.startswith('X-DSPAM-Confidence:'):
        number = float(line[length:])
        count =count+1
        sum = number + sum
print('Average spam is ', sum/count)
