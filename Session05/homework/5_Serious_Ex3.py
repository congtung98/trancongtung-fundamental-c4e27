def is_inside(pos_point,pos_rec):
    if pos_rec[0] <= pos_point[0] <= pos_rec[0]+pos_rec[2] and pos_rec[1] <= pos_point[1] <= pos_rec[1]+pos_rec[3] :
        return True
    else:
        return False

point = [20,20]
rectangle = [30,30,100,200]
if is_inside(point,rectangle):
    print('Điểm',point,'nằm trong hình chữ nhật')
else:
    print('Điểm',point,'nằm ngoài hình chữ nhật')

point_inside_rec = is_inside([200,120],[140,60,100,200])

if point_inside_rec == True:
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
