# #viết chương trình nhập n số nguyên từ bàn phím và tính tổng n số vừa nhập
# n=int(input("Mời bạn nhập n số nguyên: "))
# tong = 0
# for i in range(n):
#     so = int(input("Mời bạn nhập số "))
#     tong = tong+so
# print("Tổng n số vừa nhập là: ",tong)

# i = int(input("Mời bạn nhập vào 1 số: "))
# if i % 2 == 0:
#     print("Số bạn vừa nhập là: ",i)

# birthyear = int(input("Mời bạn nhập năm sinh của bạn: "))
# age = 2019 - birthyear
# if age < 10:
#     print("Baby")
# elif age < 16:
#     print("Teen")
# else:
#     print("Adult")

# yob = input("Nhập năm sinh: ")
# while not yob.isdigit():
#     print('Nhập sai mời bạn nhập lại!')
#     yob = input("Nhập năm sinh: ")
# age = 2019 - int(yob)
# print('Tuổi của bạn là',age)

# password = input("Nhập mật khẩu của bạn: ")
# while len(password) <= 8:
#     print('Mật khẩu phải trên 8 ký tự, mời bạn nhập lại!')
#     password = input("Nhập mật khẩu của bạn: ")
# print('Mật khẩu của bạn là',password)

# i=0
# while i < 3:
#     print(i)
#     i+=1

# loop_count = 0
# while True:
#     print('loop count:',loop_count)
#     loop_count+=1
#     if loop_count>=3:
#         break

# import math
# a = int(input("Nhập hệ số a: "))
# b = int(input("Nhập hệ số b: "))
# c = int(input("Nhập hệ số c: "))
# delta = b**2 - 4*a*c
# if delta < 0:
#      print("Phương trình vô nghiệm")
# elif delta == 0:
#     x = -b/2*a
#     print("Phương trình có nghiệm kép: x=",x)
# else:
#     x1 = (-b + math.sqrt(delta))/(2*a)
#     x2 = (-b - math.sqrt(delta))/(2*a)
#     print("Phương trình có 2 nghiệm phân biệt: x1=",x1,"x2=",x2)

ls=[]
n = int(input("Mời bạn nhập số phần tử: "))
for i in range(n):
    print("Nhập phần tử thứ",i)
    so = int(input(""))
    ls.append(so)
print("Dãy bạn vừa nhập là:")
print(ls)

print("Tổng dãy vừa nhập:")
print(sum(ls))

print("Phần tử thứ 2 trong dãy:")
print(ls[1])