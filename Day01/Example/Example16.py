lst = ['alpha', 'bravo', 'charlie', 'delta', 'echo']
for c in lst:
    print(c[:1])

for idx, string in enumerate(lst):
    print("%s has an index of %d" %(string, idx))


for i in range(2, 4):
    print("lst at %d contains %s" %(i, lst[i]))

lst = ['alpha', 'bravo', 'charlie', 'delta', 'echo']

for s in lst [1 :: 2]:
    print(s)

for i in range(1, len(lst), 2):
    print(lst[i])