from turtle import *

def say_hello_world():
    for i in range(3):
        print('Hello world')

say_hello_world()

def sum_two_number(num1,num2):
    sum = num1 + num2
    print(sum)

sum_two_number(1,2)

def draw_square(length,color_line):
	color(color_line)
	for i in range(4):
		forward(length)
		left(90)

draw_square(100,'black')

for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

def draw_star(x,y,length):
	penup()
	setx(x)
	sety(y)
	pendown()
	for i in range(5):	
		right(144)	
		forward(length)

speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)

draw_star(0,200,200)

mainloop()