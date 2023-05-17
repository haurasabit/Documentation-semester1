# LIST 
# -general purpose
# -most widely used data structure
# -grow and shrink size as needed
# -sequence type
# -sortable

# CONSTRUCTORS ---> creating a new list
x = list()
y = ['a', '25', 'dog', 8.43]
tuple1 = (10, 20)
z = list(tuple1)
print(z)

# list comprehension
a = [m for m in range(8)]
print(a)
b = [i**2 for i in range(10) if i>4]
print(b)