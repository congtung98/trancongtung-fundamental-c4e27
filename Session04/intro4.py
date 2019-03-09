# colors = ['red','green','blue','black']
# b = colors

# b[0] = 'yellow'
# print(colors[0])

# #3 cách khởi tạo danh sách
# a = []

# a = [1,2,3]

# a = list(range(3))

# print(a)

# #3 cách thêm dữ liệu vào danh sách
# a.append(3)

# print(a)

# a.insert(0,"Hello")

# a.extend(b)

# print(a)

# #Update list
# a[1] = 'Bye'

# print(a)

# #Delete list
# del_element = a.pop(5)
# print(del_element)

# del a[7]
# print(a)

# a.remove('Hello')
# print(a)

# #Slices
# ls = ['a','b','c','d','e']

# print(ls[1:-2])

# n = int(input("Nhập n: "))
# ds = []
# for i in range(n):
#     so = int(input("Mời bạn nhập số: "))
#     ds.append(so)
# print("Danh sách số vừa nhập:",ds)

# for i in range(n):
#     for j in range(i+1,n):
#         # print('Các cặp số là: ',ds[i],'',ds[j])
#         check = ds[i] + ds[j]
#         if check%2 == 0:
#             print('Cặp số có tổng chẵn là: ',ds[i],'',ds[j])

# n=100
# for x in range(n):
#     for y in range(x+1,n):
#         for z in range(y+1,n):
#             if (x**2+y**2+z**2) == x*y*z:
#                 print('Bộ 3 số cần tìm là: ',x,y,z)
    
#Dictionary
#Init dict:
# dic = {}

# dic = dict()

# dic = {'name':'Trần Công Tùng','age':21}
#Create
# person = {"name":"Trần Công Tùng","age":21}
# person['age']=29
# person['addr']='Hà Nội'
# # age=person['age']
# # print(age)
# addr=person.get('address','không có')
# if 'address' in person:
#     addr=person['address']
# print(addr)

tu_dien = {'computer':'Máy tính','mouse':'Chuột','keyboard':'Bàn phím'}
print('Chào mừng bạn đến với từ điển 4.0. Muốn thoát ứng dụng xin mời nhập "exit"')
while True:
    search = input('Mời bạn nhập từ cần tra: ')
    if search == 'exit':
        break
    elif search in tu_dien:
        print(search,'nghĩa là',tu_dien[search])
    else:
        print('Từ này không có trong từ điển. Bạn muốn thêm nghĩa cho nó không?')
        choice = input('Nhập yes để thêm nghĩa, nhập phím bất kì để tra từ khác: ')
        if choice == 'yes':
            explain = input("Nhập nghĩa từ cần thêm: ")
            tu_dien[search] = explain
        else:
            break

# tap_nguoi=[]
# nguoi_1={
#     "name":"nguyen van a",
#     "age":12,
#     "add":"ha noi",
#     "sdt":["0123","43434"]
# }
# tap_nguoi.append(nguoi_1)
# nguoi_2={
#     "name":"nguyen van b",
#     "age":12,
#     "add":"ha noi",
#     "sdt":["0123","43434"]
# }
# tap_nguoi.append(nguoi_2)
# # print(tap_nguoi)   
# # print(tap_nguoi[0]['age'])
# for v in tap_nguoi:
#     print(v['name'])
