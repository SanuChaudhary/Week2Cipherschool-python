user_info={
    'name':'Mohit',
    'age':18,
    'section':'KOC12',
    'stream':'cse',
}
#to add data
user_info['Address']=["Jhunjhunu"]
print(user_info)

#to delete
#pop method
popped_item = user_info.pop("section")
print(f"popped item is {popped_item}")
print(user_info)
print(type(popped_item))

# popitem method
popped_item = user_info.popitem()
print(user_info)
print(type(popped_item))