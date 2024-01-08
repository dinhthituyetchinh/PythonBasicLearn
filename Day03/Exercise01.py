cotDiem01 = float(input("Nhập cột điểm thứ nhất: "))
cotDiem02 = float(input("Nhập cột điểm thứ hai: "))
cotDiem03 = float(input("Nhập cột điểm thứ ba: "))
cotDiem04= float(input("Nhập cột điểm thứ tư: "))

dtb = (cotDiem01 + cotDiem02 + cotDiem03 + cotDiem04) / 4;

print("Điểm trung bình là: ")
print(dtb)
print("Điểm hệ chữ là: ")
if dtb > 8.5:
    print ("A")
elif dtb > 7.0:
    print("B")
elif dtb > 5.5:
    print("C")
elif dtb > 4.0:
    print("D")
else:
    print ("F")