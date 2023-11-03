i = 0
while i < 7:
    print (i)
    if i == 4:
        print("Breaking from loop")
        break
    i += 1

for i in range(4):
    print(i)
    if i == 2:
        break


for i in range(6):
    if i == 2 or i == 4:
        continue
    print(i)


while True:
    for i in range(1, 5):
        if i == 2:
            break

def break_loop():
    for i in range(1,5):
        if(i == 2):
            return (i)
        print(i)
    return (5)

print(break_loop())