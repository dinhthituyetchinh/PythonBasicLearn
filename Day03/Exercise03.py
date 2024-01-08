num = int(input("Nhap 1 ky tu cua he thap luc phan: "))

def case0():
    return 0

def case1():
    return 1

def case2():
    return 2

def case3():
    return 3

def case4():
    return 4

def case5():
    return 5

def case6():
    return 6

def case7():
    return 7

def case8():
    return 8

def case9():
    return 9

def caseA():
    return "A"

def caseB():
    return "B"


def caseC():
    return "C"


def caseD():
    return "D"


def caseE():
    return "E"


def caseF():
    return "F"

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
        9: case9,
        10: caseA,
        11: caseB,
        12: caseC,
        13: caseD,
        14: caseE,
        15: caseF
    }

    selected_case = switch_dict.get(num, default)

    result = selected_case()
    return result

print("Tương đương với hệ thập phân là:")
print(switch_case(num))
