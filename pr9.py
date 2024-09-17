# TUPLE IN PYTHON
# Tuples are immutable in Python, meaning you can't modify them once they're created.

a = ()
print(type(a))


# TUPLE METHODS

my_tuple = (2, 3, 'jaydip', 3)
print(my_tuple.count(3)) # Output 2
print(my_tuple.index('jaydip')) # Output 2


# Tuple Packing and Unpacking

# Packing
Myt = ( 2, 4, 'student')

# Unpacking
a, b, c =Myt
print(a)
print(b)
print(c)


# Concatenation

tup1 = (1, 2, 'jaydip', 4, 5)
tup2 = (6, 7, 'manek', 9)
result = tup1 + tup2
print(result) # Output : (1, 2, 'jaydip', 4, 5, 6, 7, 'manek', 9)


# Length of a Tuple

tp = ('jaydip', 1, 2, 3, False)
print(len(tp)) # Output : 5

#  Slicing

tp2 = (1, 2, "jaydip", 4)
print(tp2[0:3])


# Repetition

tp3 = (1, 2, 3)
tp4 = tp3 *10
print(tp4)
# Output : (1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)