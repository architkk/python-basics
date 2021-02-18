"""
Input Description:
The inputs are two natural numbers representing the length and the breadth of a rectangle.

Output Description:
Find the area of the rectangle formed by the provided input. Round off the answer to the first decimal place if required.

Sample Input :
2
3
Sample Output :
6
"""

num1 = float(input(""))
num2 = float(input(""))
if num1<0 or num2<0:
    print("Error")
else:
    num3 = num1*num2
    print(round(num3,1))