n = int(input("Nhập số nguyên: "))
sum = 0

for i in range(1, n + 1):
    sum += 1.0 / ((i + 1) * i)

print("Tong: {:.2f}".format(sum))
