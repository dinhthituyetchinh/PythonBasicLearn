from array import *
a = array('i', [1,2, 3, 4, 5])
print(a[1]) #Xuất phần tử ở vị trí 1
# Xuất mảng
for i in a:
    print(i)
#Thêm phần tử vào cuối mảng
from array import *
a = array('i', [1,2, 3, 4, 5])
a.append(6)
for i in a:
    print(i)
#Thêm/ chèn phần tử mới vào một vị trí nào đó
from array import *
a = array('i', [1,2, 3, 4, 5])
a.insert(3, 9)
for i in a:
    print(i)
#Nối hai mảng
from array import *
a = array('i', [1,2, 3, 4, 5])
b = array('i', [7, 8, 9, 10])
a.extend(b)
for i in a:
    print(i)
#Thêm phần tử từ list vào array

from array import *
a = array('i', [1,2, 3, 4, 5])
c = [11, 12, 13]
a.fromlist(c)
for i in a:
    print(i)

#Xoá bất kì phần tử nào của mảng

from array import *
a = array('i', [1,2, 3, 4, 5])
a.remove(4)
for i in a:
    print(i)

#Xoá phần tử cuối mảng
from array import *
a = array('i', [1,2, 3, 4, 5])
a.pop()
for i in a:
    print(i)

#Tìm bất kì vị trí phần tử nào sử dụng index
from array import *
c = array('i', [11, 12, 13, 14, 15])
print(c.index(11))
# Đảo ngược mảng
from array import *
a = array('i', [1,2, 3, 4, 5])
a.reverse()
for i in a:
    print(i)
#Địa chỉ(bộ đệm) trong bộ nhớ của mảng và số phần tử trong mảng
from array import *
c = array('i', [11, 12, 13, 14, 15])
print(c.buffer_info())
#Đếm số phần tử trong mảng
from array import *
c = array('i', [11, 11, 13, 11, 15])
print(c.count(11))
#Chuyển chuỗi thành mảng/ chuỗi thành mảng
from array import *
my_char_array = array('c', ['g','e','e','k'])
# array('c', 'geek')
print(my_char_array.tostring())

#Chuyển mảng  thành list
from array import *
a = array('i', [1, 2, 3, 4, 5])
c = a.tolist()
print(a)
print(c)
# Thêm chuỗi vào mảng kí tự
from array import *
my_char_array = array('c', ['g','e','e','k'])
my_char_array.fromstring("stuff")
print(my_char_array)