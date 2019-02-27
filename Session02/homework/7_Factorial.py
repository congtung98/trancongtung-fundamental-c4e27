number = int(input("Enter your number to calculate factorial of it: "))
factorial = 1
for x in range(1,number+1):
    factorial = factorial * x
print("Factorial of n: ",factorial)