# generate list with range function
numbers = list(range(1,11))
print(numbers)

#pop method
popped_item = numbers.pop()
print(numbers)

#index method
numbers=[1,2,3,4,5,6,7,8,9,10,1,5,7,1]
print(numbers.index(1, 3))
print(numbers.index(1, 11))
print(numbers.index(1))
print(numbers.index(1, 11, 14))

#pass list to a function
def negative_list(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative
print(negative_list(numbers))