a = 2
print(a)
print(type(a))
b = 9223372036854775807
print(b)
print(type(b))
pi = 3.14
print(pi)
print(type(pi))
c = 'A'
print(c)
print(type(c))
name = 'Dinh Thi Tuyet Chinh'
print(name)
print(type(name))
q = True
print(q)
print(type(q))
x = None
print(x)
print(type(x))

m, n, o = 1, 2, 3
print(m, n, o)

m, n, _ = 1, 2, 3
print(m, n)

m = n = o = 1
print(m, n, o) # Output 1 1 1
n = 2 
print(m, n, o) #Output 1 2 1 => Câu lệnh sau có thể lấy kết quả từ câu lận trước
                # miễn là câu lệnh trước được thực thi, xong mới thực thi câu lệnh sau
                