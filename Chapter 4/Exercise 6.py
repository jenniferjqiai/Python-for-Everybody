# Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters
# (hours and rate).

def computepay ( hours, rate):
    if hours <= 40 :
        pay = hours * rate
    else:
        pay = hours*rate+(hours-40)*rate*0.5
        return pay 
x = computepay(45,10)
print(x)
