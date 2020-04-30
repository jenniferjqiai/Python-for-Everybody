# Write a program that reads a file and prints the letters in decreasing order of frequency.
# Your program should convert all the input to lower case and only count the letters a-z.
# Your program should not count spaces, digits, punctuation, or anything other than the letters a-z.
# Find text samples from several different languages and see how letter frequency varies between languages.
# Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.
import string

fname=input('Enter a file name :')
try:
    fhand=open(fname,'r')
except:
    print(fname,'cannot be opened')
    exit()

alphabet='abcdefghijklmnopqrstuvwxyz'
count=dict()
letter=list()
for line in fhand:
    line=line.translate(line.maketrans('','',string.punctuation))
    line=line.lower()
    line=line.split()
    for t in line:
        words=list(t)
        for l in words:
            if l in alphabet:
                count[l] = count.get(l, 0) + 1
letter=list()
for k,v in (count.items()):
    newt= (v,k)
    letter.append(newt)
letter = sorted(letter,reverse=True)
for v,k in letter:
    print(k,v)
