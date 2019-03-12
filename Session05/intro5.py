# m = int(input('Nhập m: '))
# tong = 0
# for i in range(m): 
#     so = int(input('Nhập số: '))
#     tong += so
# print('Tổng dãy số vừa nhập:',tong)

# n = int(input('Nhập n: '))
# tong = 0
# for i in range(n):
#     so = int(input('Nhập số: '))
#     tong += so
# tbc = tong/n
# print('Trung bình cộng dãy vừa nhập là:',tbc)

# def say_hi():
#     print('hi')
#     print('bye')
# say_hi()

# def add_two_number(a,b):
#     print('Tổng hai số là:',a+b)

# num1 = int(input('Nhập số thứ nhất: '))
# num2 = int(input('Nhập số thứ hai: '))
# add_two_number(5,5)

# def add_two_number(a,b):
#     return a+b

# num1 = int(input('Nhập số thứ nhất: '))
# num2 = int(input('Nhập số thứ hai: '))
# num3 = int(input('Nhập số thứ ba: '))

# sum_1_2 = add_two_number(num1,num2)
# sum_3 = add_two_number(sum_1_2,num3)
# print('Tổng 3 số là:',sum_3)

# def abs_of_number(a):
#     if a > 0:
#         return a
#         print('Giá trị tuyệt đối là:',a)
#     else:
#         return -a
#         print('Giá trị tuyệt đối là:',-a)
#     print('Trị tuyệt đối là:',a)

# x = abs_of_number(-12)
# tong = 12 + abs_of_number(-12)
# print(x)
# print(tong)

# def evaluate(num1,num2,operator):
#     if operator == '+':
#         return num1+num2
#     elif operator == '-':
#         return num1-num2
#     elif operator == '*':
#         return num1*num2
#     elif operator == '/':
#         return num1/num2
#     else:
#         return None

# x = evaluate(3,4,'*')
# print(x)

def check_prime(number):
    if number < 2:
        return False
    for v in range(2,number):
        if number % v == 0:
            return False
    return True

so = int(input('Nhập số cần kiểm tra:'))

for v in range(2,so+1):
    if check_prime(v):
        print('Số nguyên tố là:',v)
# if check_prime(so):
#     print('Là số nguyên tố')
# else: 
#     print('Không là số nguyên tố')

