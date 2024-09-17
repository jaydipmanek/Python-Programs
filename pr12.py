# Loops In Python

for j in range(1, 11):
    print(j)


j = 1
while(j<102):
    print("jaydip")
    j +=1



k = [1, 2, 4, 5, 10]
for i in k:
    print(i)



# For Loop with else

l = [2, 3, 4, 20]
for i in l:
    print(i)
else:
    print('End')


# The break Statement
for i in range(0, 100):
    if i == 34:
        break # Exit the loop 
    print(i)



# The Continue Statement
for j in range(0, 100):
    if j == 34:
        continue # Skip iteration
    print(j)


# The pass Statement
# pass is the null statement in the python

l  = [1, 2, 4]
for item in l:
    pass