n = int(input("Nhập số nguyên: "))
sum = 1

for i in range(1, n + 1):
    sum += 1.0 / (2 * i + 1)

print("Tong: {:.2f}".format(sum))
