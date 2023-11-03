for i in range (4):
    print(i)
else:
    print ('done')


i = 0
while i < 3:
    print(i)
    i += 1
else:
    print('done')


for i in range (3):
    print(i)
    if i == 1:
        break
else:
    print ('done')


a = [1, 2, 3, 4]
for i in a:
    if type(i) is not int:
        print(i)
        break
else:
    print("no exception")

for x in range(10):
    pass ##we don't want to do anything, or are not ready to do anything here, so we'll pass
