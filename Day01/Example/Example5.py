# x or y
# x and y
# not x

names = ['Alice', 'Bob', 'Craig', 'Diana', 'Eric']
print(names[0]) 
print(names[2]) 

print(names[-1])
print(names[-4]) 

names[0] = 'Ann'
print(names)

names.append("Sia") #Append object to end of list 
print(names)

names.remove("Bob")
print(names)


names.insert(1, "Nikki") #Add a new element to list at a specific index
print(names)

names = ['Alice', 'Bob', 'Craig', 'Diana', 'Eric']
index = names.index("Diana")
print(index)

print(len(names)) #Count length of list

names = ['Alice', 'Bob', 'Craig', 'Diana', 'Eric']
print(names.pop())

a = [1, 1, 1, 2, 3, 4]

print(a.count(1))

a.reverse()
print(a)
# Hoặc 
a[::-1]
print(a)
