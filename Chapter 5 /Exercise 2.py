# Write another program that prompts for a list of numbers as above
# and at the end prints out both the maximum and minimum of the numbers instead of the average.
largest=None
smallest=None
while True:
    line = input('Enter:')
    if line != 'done':
        try:
            int(line)
        except:
            print('Please enter a number')
            continue
        if largest is None or line >largest :
            largest=line
            if smallest is None or line < smallest:
                smallest=line
            continue
    if  line == 'done' :
        print('Max:', largest,'Min',smallest)
        break