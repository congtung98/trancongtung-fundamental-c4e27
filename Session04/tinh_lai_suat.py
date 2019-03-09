import math
money_invest = int(input('Mời bạn nhập số tiền gửi ngân hàng: '))

interest_rate = 0.065 
time = 9
money_grow = money_invest*(1+interest_rate)**time
print('Số tiền trong tài khoản của bạn sau 9 năm là:',money_grow)
x = 1200/21
y = 1+interest_rate
time = math.log(y)/math.log(x)
print('Số năm bạn cần gửi để có 1.2 tỷ trong tài khoản là:',time)

# money = int(input('tiền đang có : '))
# year = int(input('năm nuôi tiền @@ : '))

# for i in range (1,year+1):
#     money = money + (6.5/100)*money
# print('số tiền qua',i,'năm : ',money) 

# n = 0 
# savemoney = int(input('tiền đang có : ' ))
# while not savemoney > 1200000000 :
#     savemoney =savemoney + (6.5/100)*savemoney
#     n = n +1
# print('số năm để tiết kiệm được 1,2 tỉ là ',n)