# Why should we use functions at all?

# The first reason is reusability. 
# Once a function is defined, it can be used over and over and over again. 
# You can invoke the same function many times in your program, which saves you work. 
# Imagine what programming would be like if you had to teach the computer about sines every time you needed to find the sine of an angle! 
# You'd never get your program finished!

# Another aspect of reusability is that a single function can be used in several different (and separate) programs. 
# When you need to write a new program, you can go back to your old programs, find the functions you need, and reuse those functions in your new program. 
# You can also reuse functions that somebody else has written for you, such as the sine and cosine functions.

# The second reason is abstraction. In order to use a particular function you need to know the following things:

# 1.The name of the function;
# 2.What the function does;
# 3.What arguments you must give to the function; and
# 4.What kind of result the function returns.

# How to define/declare a function?

# Step 1: Declare the function with the keyword def followed by the function name.
# Step 2: Write the arguments inside the opening and closing parentheses of the function, and end the declaration with a colon.
# Step 3: Add the program statements to be executed.
# Step 4: End the function with/without return statement.

# How to call/use a function?

# We just simply write a function and after defined it, we write them in the program
# EX: Function definition
# def defaultArg( name, msg = "Hello!"):
#     Function call
# defaultArg(name)

# What is return, why and how do we use it?

# The return statement causes your function to exit and hand back a value to its caller. 
# The point of functions in general is to take in inputs and return something. 
# The return statement is used when a function is ready to return a value to its caller.

# Do we have to use return in every function?

# No, it is not necessary. 
# The function returns after the last line. 
# There is no difference between a simple return and no return.

# What are function arguments/parameters, why and how we use it?

# Most functions require arguments: the arguments provide for generalization. For example, if we want to find the
# absolute value of a number, we have to indicate what the number is. Python has a built-in function for computing the
# absolute value:
# >>> abs(5)
# 5
# >>> abs(-5)
# 5
# In this example, the arguments to the abs function are 5 and -5.
# Some functions take more than one argument. For example the built-in function pow takes two arguments, the base
# and the exponent. Inside the function, the values that are passed get assigned to variables called parameters.
# >>> pow(2, 3)
# 8
# >>> pow(7, 4)
# 2401

# How to use function from a different file other than our currently working file?

# Just write from file import function, and then call the function using function(a, b). 
# The reason why this may not work, is because file is one of Python's core modules, 
# so I suggest you change the name of your file.

# Note that if you're trying to import functions from a.py to a file called b.py, 
# you will need to make sure that a.py and b.py are in the same directory.