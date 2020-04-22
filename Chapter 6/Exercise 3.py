# Encapsulate this code in a function named count,
# and generalize it so that it accepts the string and the letter as arguments.

def count (word, theletter):
    number = 0
    for letter in word:
        if letter == theletter:
           number = number+1
    print (number)
count('apple','p')