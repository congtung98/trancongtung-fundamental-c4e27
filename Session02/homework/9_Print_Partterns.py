for i in range(20):
    print("*",end=' ')
print()
n = int(input("Enter your number of stars: "))
for i in range(n):
    print("*",end=' ')
print()
for i in range(4):
    print("x",end=' * ')
print("x")
n = int(input("Enter a number: "))
if n%2 == 0:
    for i in range(int(n/2)):
        print("x",end=' * ')
else:
    for i in range(int((n-1)/2)):
        print("x",end=' * ')
    print("x")
print()
for i in range(3):
    for j in range(7):
        print("*",end=' ')
    print()
print()
n = int(input("Enter n: "))
m = int(input("Enter m: "))
print()
for i in range(m):
    for j in range(n):
        print("*",end=' ')
    print()