# List
a = [1, 2, 3, 4]
print(type(a))

# Tuple
# immutable and it is index based
b = (1, 2, 3, 2, 5, 2, 4)
# To find the index value of particular value in the tuple
print(b.index(2, 2))
# slice operator to print the values
print(b[0])
# count
print(b.count(2))
# max
print(max(b))
# min
print(min(b))
# we can concat with only a tuple
print(b + (2, 3, 4))
x = set(b)
print(x)
print(type(x))

# Set
c = {1, 2, 3, 4}

# Dict
d = {1: "vanan", 2: "mathi"}
print(type(d))
