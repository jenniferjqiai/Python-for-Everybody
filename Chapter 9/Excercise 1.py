file = open('words.txt','w')
line1 = 'Writing programs or programming is a very creative'
file.write(line1)
file.close()
# Write a program that reads the words in words.txt and stores them as keys in a dictionary.
# It doesn’t matter what the values are.
# Then you can use the in operator as a fast way to check whether a string is in the dictionary
fhand=open('words.txt')

dictionary = dict()
file=open('words.txt')
for line in file :
    words = line.split()
for word in words:
    dictionary[word]=dictionary.get(word,0)+1
var=input("Please enter a word:")
if  var in dictionary:
    print(var,'is in the dictionary')
else:
    print(var, 'is not in the dictionary')
