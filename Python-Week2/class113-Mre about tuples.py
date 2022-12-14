mixed = (1,2,3,4.0)
for i in mixed:
    print(i)

print(type(mixed))

nums=(1,)
words=("word1",)
print(type(nums))
print(type(words))
# tuple without parenthesis
guitars = "yamaha","baton rouge" ,"taylor"
print(type(guitars))
# tuple unpacking
guitarists = ("maneli Jamal","Eddie Van Der Meer","Andrew Foy")
guitarist1 ,guitarist2,guitarist3 = (guitarists)
print(guitarist1)

# list inside tuples
favourites = ("southern magnolia" , ["tokyo Ghoul Theme", "landscape"])
favourites[1].pop()
favourites[1].append("we made it")
print(favourites)

#min(),max,sum
print(min(mixed))
print(max(mixed))
print(sum(mixed))