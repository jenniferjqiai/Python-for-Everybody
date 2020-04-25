# To compute the average
numlist=list()
while (True):
    inp= input("Enter a number :")
    if inp=='done':
        break
    try:
        value= float(inp)
        numlist.append(value)
        average = sum(numlist) / len(numlist)
        print(average)
    except:
        average=0
print('devide by zero')


# delimiter
t=['printing','for','the','fjords']
delimiter=' '
delimiter.join(t)
print(t)

#t=['printing','for','the','fjords']
#delimiter=' '
#t.join(delimiter)
#print(t)
# Traceback (most recent call last):
#  File "/Users/jqiai/Documents/CS/Chapter 8/Test.py", line 20, in <module>
#    t.join(delimiter)
# AttributeError: 'list' object has no attribute 'join'


# try tail function
def bad_move_head(t):
    del t[1:]
sale=[1,2,3]
s=bad_move_head(sale)
print(s)
deal=[1,2,3]
def tail(d):
    return d[1:]
print(sale)
hot=tail(deal)
print(hot)
print(deal)