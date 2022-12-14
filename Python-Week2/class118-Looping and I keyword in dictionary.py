user_info={
    'name':'Mohit',
    'age':18,
    'section':'KOC12',
    'stream':'cse',
}

if 'name' in user_info:
    print("present")
else:
    print("not present")
# to check value or complete list
if 'Mohit' in user_info.values():
    print("present")
else:
    print("not present")

# loops in dictionary
for i in user_info.values():
    print(i)

#values method
user_info_values = user_info.values()
print(user_info_values)
print(type(user_info_values))

#keys method
user_info_keys = user_info.keys()
print(user_info_keys)
print(type(user_info_keys))

# loops in dictionaries
for i in user_info:
    print(user_info[i])

# items method
user_items = user_info.items()
print(user_items)
print(type(user_items))

for key , value in user_info.items():
    print(f"key is {key} and value is {value}")