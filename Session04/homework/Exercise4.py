print('Trả lời câu hỏi toán học sau:')

tap_quiz = []

quiz_1 = { "Q:": "Nếu x = 8, vậy thì kết quả của 4(x+3) là?", 1:35,2:36,3:40,4:44}
quiz_2 = {"Q:": "Nếu Jack được các điểm số trong bài test sau: 49, 81, 72, 66 and 52. Điểm số trung bình là?",
            1:"Khoảng 55",
            2:"Khoảng 65",
            3:"Khoảng 75",
            4:"Khoảng 85"}

tap_quiz.append(quiz_1)
tap_quiz.append(quiz_2)

so_lan_dung = 0

for k,v in quiz_1.items():
    print(k,v,sep='.')
lua_chon = int(input('Lựa chọn của bạn: ')) 
if lua_chon == 4:
    print('Bingo')
    so_lan_dung += 1
else:
    print(':(')

for k,v in quiz_2.items():
    print(k,v,sep='.')
lua_chon = int(input('Lựa chọn của bạn: ')) 
if lua_chon == 2:
    print('Bingo')
    so_lan_dung += 1
else:
    print(':(')

print('Bạn trả lời đúng',so_lan_dung,'trên',len(tap_quiz),'câu hỏi')
