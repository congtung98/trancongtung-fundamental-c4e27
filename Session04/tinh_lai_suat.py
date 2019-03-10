import math
money_invest = int(input('Mời bạn nhập số tiền gửi ngân hàng: '))

interest_rate = 0.065 
time = 9
money_grow = money_invest*(1+interest_rate)**time
print('Số tiền trong tài khoản của bạn sau 9 năm là:',money_grow)
x = 1200/21
y = 1+interest_rate
time = math.log(x,y)
print('Số năm bạn cần gửi để có 1.2 tỷ trong tài khoản là:',time)


