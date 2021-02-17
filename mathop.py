"""
This is a syntax for multiple line comments. Here we will learn about numbers and operators in python
"""
# NUMBERS
x = 1 # int
y = 1.2 # float
z = 1+2j # complex number

# To find the type of the number
print(type(x))
print(type(y))
print(type(z))

# Converting number to another type
a = float(x) #converting int to float
b = int(y)  #converting float to int
c = complex(y) #converting float to complex
print(a)
print(b)
print(c)

# OPERATIONS
E = 11
F = 23

# Math Operations
A = E+F #Addition
S = E-F #Subtraction
M = E*F #Multiplication
D = E/F #Division
Mod = E%F #Modulo Division
Exp = E**F #E^F
Floor = E//F #Floor Division - Round off result to nearest intiger
print(A)
print(S)
print(M)
print(D)
print(Mod)
print(Exp)
print(Floor)

"""
Common Errors in Python

Syntax Error - print "Hello"
Index Error - let a = [1,2,3] now a[3] is an index error
Module Not Found Error -  Due to missing Module
Key Error - Consider a dictionary d = {'1':"arc", '2':"hit"}. Now d[3] will give key error
Import Error - If an item from a module is imported which doesnt exist
Stop Iteration Error - Consider it = itr([1,2,3]). Iterating for the fourth time using next(it) wil give this error
Type Error - "12"+12 will give this error as "12" is a string and 12 is a number
Value Error - int("xyz")
Name Error - If a variable is not defined then a name error is thrown
Zero Division error - 100/0 
Keyboard Interrupt Error - Ctrl+C gives this error as the program is interrupted
Indentation Error - Applicable for loops as python doesnt have opening and closing brackets

"""
