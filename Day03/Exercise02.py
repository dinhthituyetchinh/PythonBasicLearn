num = int(input("Nhap 1 so bat ky (0 -> 9): "))

def case0():
    return "Không"

def case1():
    return "Một"

def case2():
    return "Hai"

def case3():
    return "Ba"

def case4():
    return "Bốn"

def case5():
    return "Năm"

def case6():
    return "Sáu"

def case7():
    return "Bảy"

def case8():
    return "Tám"

def case9():
    return "Chín"

def default():
    return "Bạn nhập không hợp lệ"

def switch_case(num):
    switch_dict = {
        0: case0,
        1: case1,
        2: case2,
        3: case3,
        4: case4,
        5: case5,
        6: case6,
        7: case7,
        8: case8,
        9: case9
    }

    selected_case = switch_dict.get(num, default)

    result = selected_case()
    return result


print(switch_case(num))
