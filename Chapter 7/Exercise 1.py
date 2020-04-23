newfile=open('mbox-short.txt','w')
line1='From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008\n '
newfile.write(line1)
newfile.close()
shout = input('Enter a file name:')
file=open(shout)
U=file.read()
print(U.upper())