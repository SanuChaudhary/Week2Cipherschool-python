
def greater(a,b):
    if a > b:
        return a
    else:
        return b

def greatest(a,b,c):
    if a> b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

# function inside function
#greater(a,b)--> a or b
# greater(a,b,c)--->greatest

def new_greatest(a,b,c):
    # bigger = greater(a,b)
    return greater(greater(a,b),c)
print(new_greatest(10,20,30))