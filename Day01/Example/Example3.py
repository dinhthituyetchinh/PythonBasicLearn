x = y = [7, 8, 9]
print(x)
x = [13, 8, 9]
print(y)
print(x)

x = y = [7, 8, 9]
x[0] = 13
print(y)
#Nested lists are also valid in python
x = [1, 2, [3, 4, 5], 6, 7]
print(x)
print(x[2])
print (x[2][1])