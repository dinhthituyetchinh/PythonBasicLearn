def my_function():
    a = 2
    return a
    my_function() # Close func
print(my_function()) #Output

a = int(input("a: "))
b = int(input("b: "))
if a > b:
    print (a)
else:
    print (b)


if a > b: print (a)
else: print(b)

# An empty block causes an IndentationError. Use pass (a command that does nothing) 
# when you have a block with no content:

def willBeImplementedLater():
    pass

