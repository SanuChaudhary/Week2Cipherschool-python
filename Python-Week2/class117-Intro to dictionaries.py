user = ["Mohit",18,["kimi no na wa"],["awakening","fairy tale"]]
# you can do this but this is not a good way
user= {"name":"Mohit","age":18}
print(user)
print(type(user))

# 2nd method
user1 = dict(name = "Mohit", age=18)
print(user1)

#to access data in dictionary
print(user["name"])
print(user["age"])

# what we can store in dictionary
#anything
# number,strings,list,dictionary

user_info={
    'name':'Mohit',
    'age':18,
    'section':'KOC12',
    'stream':'cse',
}
print(user_info["section"])

user_info2 = {}
user_info2['name']='Mohit Chaudhary'
user_info2['age']='18'

print(user_info2)