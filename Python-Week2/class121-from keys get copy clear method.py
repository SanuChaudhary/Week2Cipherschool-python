d = {"name":"unkown" , "age":"unknown"}

d=dict.fromkeys(range(1,11),"unkown")
print(d)

d=dict.fromkeys(["name","age"],"unkown")
print(d)

# get method
d = {"name":"Mohit", "age":18}
print(d["name"])

if 'name' in d:
    print("present")
else:
    print("not present")

if d.get("names"):
    print("present")
else:
    print("not present")

d.clear()
print(d)

d1 = d.copy()
print(d1)

d1=d
print(d1.popitem())
print(d)

print(d1 is d)