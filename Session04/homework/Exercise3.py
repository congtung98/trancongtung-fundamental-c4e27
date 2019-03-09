print('Trả lời câu hỏi toán học sau:')

quiz = { "Q:": "Nếu x = 8, vậy thì kết quả của 4(x+3) là?", 1:35,2:36,3:40,4:44}
for k,v in quiz.items():
    print(k,v,sep='.')
lua_chon = int(input('Lựa chọn của bạn: ')) 
if lua_chon == 4:
    print('Bingo')
else:
    print(':(')
