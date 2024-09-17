
# Dictionary And Sets

Student_info = {
    "Name":  "jaydip",
    "Age":   20,
    "course": "Python",
    "Marks": [70, 29, 40]



}
print(Student_info, type(Student_info))



# Dictionary Methods

my_dict = {'name': 'Jaydip', 'age': 22}
print(my_dict.get('name'))  # Output: Jaydip
print(my_dict.get('address', 'Not Found'))  # Output: Not Found
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
my_dict.update({'Address': 'dwarka', 'age': 20})
print(my_dict)
my_dict.pop('name')
print(my_dict)
my_dict.popitem()
print(my_dict)

my_new = my_dict.copy()
print(my_new)
my_new.clear()
print(my_new)

my_new.update({'name': 'jaydip', 'age': 19})
print(my_new)

# Sets

S = {1, 2, 'jaydip'}
print(type (S)) # <class 'set'>

e = set() # Empty Set
print(type(e))

# Sets Methods

my_set = {1, 2, 3, 'jaydip', 4}
my_set.add(False)
print(my_set)

my_set.remove(False)
print(my_set)

my_set.discard(21) 
print(my_set)

manek = my_set.pop()
print(manek)

my_set.clear() 
print(my_set)

my_set.add( 122) 
print(my_set)


new_set = my_set.copy()
print(new_set)