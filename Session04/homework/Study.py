alphabet = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,
            'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
count_alphabet = {}
string = input('Mời bạn nhập một từ: ')
string = string.lower()
ls_str = list(string)

#Truyền chữ cái từ input vào ds đếm chữ cái
for i in range(len(ls_str)):
    if ls_str[i] in alphabet:
        count_alphabet[ls_str[i]] = 0
#Duyệt input và update số lượng chữ cái trong input
for i in range(len(ls_str)):
    if ls_str[i] in count_alphabet:
        count_alphabet[ls_str[i]] += 1

for k,v in count_alphabet.items():
    print(k,v,sep=' ')