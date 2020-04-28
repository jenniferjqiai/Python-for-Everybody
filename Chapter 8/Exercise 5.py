#Exercise 5: Write a program to read through the mail box data
# and when you find line that starts with “From”,
# you will split the line into words using the split function.
# We are interested in who sent the message, which is the second word on the From line.
fname=input('Enter a file name:')
fhand= open(fname)
count=0
for line in fhand:
    words=line.split()
    if len(words) == 0: continue
    if words[0] != 'From':continue
    print(eaddress)
    count=count+1
print('ther were', count,'lines in the file From as the first word')



#     for name in names :
#         if True: continue
#         wname=wname+[names]
# print(wname)
#  names = eaddress.split('.')