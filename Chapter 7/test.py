test = open('atestfile.txt','w')
line1= 'Hello World\n'
test.write(line1)
line2='Bonjour\n'
test.write(line2)
line3='Hola\n'
test.write(line3)
test.close()

example1 = open('atestfile.txt')
count = 0
for line in example1:
    count = count +1
test2=open('atestfile.txt')
review = test2.read()
print('There are ',count, 'lines in the file')
print(review)
