# function without argument
def demo():
    print("First:", "mathi")
demo()


# function with arguments
def z(x, y):
    a = x + y
    print("Second:", a)
z(5, 4)


# function with return
def x(b, c):
    a = b + c
    return a


print("Third:", x(5, 5))


# function with multiple return
def a(x, y, z):
    add = x + y + z
    mul = x * y * z
    sub = x - y
    div = x / y
    return add, mul, sub, div
m = a(12, 3, 2)
print(type(m))


# function with multiple variable
def xz(*b):
    print(b)
xz(2, 3, 4, 5, 6, 6)

# function with multiple variable (dict)
def xy(**a):
    return a
xy1 = xy(id=2, name=3, address=4, company=5, mail=6)
print(xy1)
print(type(xy1))
