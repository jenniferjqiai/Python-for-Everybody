fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()
    while len(words) != 0:
        words[0] == 'From'
        print(words[2])