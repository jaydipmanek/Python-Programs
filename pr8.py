# LIST INDEXING

'''Collection = ["jydip", 72, 30.5, False, "manek"]
print(Collection)
Collection[0] = "JAYDIP"
print(Collection[0])
print(Collection[1:4])'''

# LIST METHODS


My_list = [1, 2, 3, 4]
My_list.append ("jaydip")
My_list.extend([23, 22]) 
My_list.insert(1, 7) 
My_list.remove(7) 

print(My_list)




my_list = [1, 2, 3,3, 3, 3,   2]
index = my_list.index(2)
print(index)  # Output: 1

my_list.sort()
print(my_list)
count = my_list.count(3)
print(count)  # Output: 4




list = [1, 2, 3]
list.reverse()
print(list)


hk = ['jaydip ', 7, 8, False]
hk.clear()
print(hk)



jk = [1, 'jaydip', 2, 3]
jk.pop(1)
print(jk)