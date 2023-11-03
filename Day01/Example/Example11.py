for i in [0, 1, 2, 3, 4]:
    print(i)

for i in range(5):
    print(i)

for x in ['one', 'two', 'three', 'four']:
    print (x)

for index, x in enumerate(['one', 'two', 'three', 'four']):
    print (index, ':', x)

x = map(lambda e : e.upper(), ['one', 'two', 'three', 'four'])
# print(x) => Python 2.x
print(list(x)) #=>Python 3.x

