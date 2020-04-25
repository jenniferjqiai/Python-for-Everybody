s=[1,2,3]
d=[1,2,3,4]

def middle(t):
    return t[1:-1]
print(middle(d))

def chop(t):
    del t[0]
    del t[-1]
print(chop(s))