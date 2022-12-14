# functions practice
def last_char(name):
    return name[-1]

print(last_char("Mohit"))

def odd_even(num):
    if num%2 == 0:
        return "even"
    else:
        return "odd"

print(odd_even(9))
print(odd_even(10))

print(last_char("Mohit"))

def odd_even(num):
    if num%2 == 0:
        return "even"
    return "odd"

print(odd_even(9))
print(odd_even(10))

def is_even(num):
    if num%2 == 0:
        return True
    return False
print(is_even(9))

def is_even(num):
    return num%2 == 0
print(is_even(9))

def song():
    return "Happy birthday song"
print(song())