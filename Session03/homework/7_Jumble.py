import random

word_list = ["beast","hunter","warrior","warlock","undead","goblin","druid","assassin"]

first_quiz = random.choice(word_list)
shuffle = list(first_quiz)
random.shuffle(shuffle)

correct = first_quiz

for i in range(0,len(first_quiz)):
    print(shuffle[i],end=' ')
print()
answer = input('Your answer: ')

while True:
    if answer == correct:
        print('Dân chơi cờ nhân phẩm thứ thiệt =)))')
        break
    else:
        print('Bạn  đã chơi cờ nhân phẩm chưa, nếu chưa hãy chơi để biết đáp án :)')
        answer = input('Your answer: ')