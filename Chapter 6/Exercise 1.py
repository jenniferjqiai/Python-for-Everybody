# Write a while loop that starts at the last character in the string
# and works its way backwards to the first character in the string,
# printing each letter on a separate line, except backwards.
fruit = 'strawberry'
index = len(fruit)
print(index)
while index >0:
    letter = fruit[index-1]
    print(letter)
    index=index-1


# Becuase start from 0, the index should minus 1 