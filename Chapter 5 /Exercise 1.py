# Write a program which repeatedly reads numbers until the user enters "done".
# Once "done" is entered, print out the total, count, and average of the numbers.
# If the user enters anything other than a number, detect their mistake using try
# and except and print an error message and skip to the next number.”
#
count=0
sum=0

while True:
    line = input('Enter:')
    if line != 'done':
        try:
            int(line)
        except:
            print('Please enter a number')
            continue
        count = count + 1
        sum = sum + int(line)
        continue
    if  line == 'done' :
        print('Ave', sum /count, 'Sum', sum, 'Count', count)
        break







