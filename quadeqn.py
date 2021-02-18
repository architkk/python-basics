"""
Input Description:
Three numbers corresponding to the coefficients of x(squared), x and constant are given as an input in that particular order

Output Description:
Print the two values of X after rounding off to 2 decimal places if required.

Sample Input :
1 5 6
Sample Output :
-2.00
-3.00
"""

a,b,c = input("").split()
a = float(a)
b = float(b)
c = float(c)

dis = b*b-4*a*c
x1 = (-b+dis**0.5)/(2*a)
x2 = (-b-dis**0.5)/(2*a)
print(format(x1, '.2f')) # Alternative method to rounding off. Useful with zero padding
print(format(x2, '.2f'))