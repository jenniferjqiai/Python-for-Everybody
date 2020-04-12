# Rewrite your pay program using try and except so that your
# program handles non-numeric input gracefully by printing a message
# and exiting the program.

hours = input('Enter the hours :')
rate = input('Enter the rate:')
try:
    H = int(hours)
    R = int(rate)
    if H <= 40 :
        pay = H*R
    else :
        pay = H*R*1.5
    print('Pay', pay)
except:
    print('Error, please enter numeric input')