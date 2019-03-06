from turtle import *
speed(0)

colors = ['red', 'blue', 'brown', 'yellow', 'grey']

color(colors[0],colors[0])

begin_fill()
for i in range(2):
    forward(100)
    left(90)
    forward(150)
    left(90)
forward(100)
end_fill()

color(colors[1],colors[1])
begin_fill()
for i in range(2):
    forward(100)
    left(90)
    forward(150)
    left(90)
forward(100)
end_fill()

color(colors[2],colors[2])
begin_fill()
for i in range(2):
    forward(100)
    left(90)
    forward(150)
    left(90)
forward(100)
end_fill()

color(colors[3],colors[3])
begin_fill()
for i in range(2):
    forward(100)
    left(90)
    forward(150)
    left(90)
forward(100)
end_fill()

color(colors[4],colors[4])
begin_fill()
for i in range(2):
    forward(100)
    left(90)
    forward(150)
    left(90)
end_fill()

mainloop()