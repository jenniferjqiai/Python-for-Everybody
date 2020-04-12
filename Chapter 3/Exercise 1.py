# Rewrite your pay computation to give the employee 1.5
# times the hourly rate for hours worked above 40 hours.

hours = float(input('Enter the hours :'))
rate = float(input('Enter the rate:'))
if hours <= 40 :
    pay = hours*rate
else :
    pay = hours*rate*1.5
print('Pay',pay)

