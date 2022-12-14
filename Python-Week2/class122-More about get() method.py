user = {"name":"Mohit Chaudhary" , "age":"18" , "age":"17"}
print(user.get("name"))
print(user.get("names")) # output is none

print(user.get("fav","not found!"))
print(user) # it overlap age 18 and give output 17