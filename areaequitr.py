"""
Input Description:
The side of an equilateral triangle is provided as the input.

Output Description:
Find the area of the equilateral triangle and print the answer up to 2 decimal places after rounding off.

Sample Input :
20
Sample Output :
173.21
"""

num = float(input(""))
if num<0:
    print("Error")
else:
    area=(1/4)*((3**0.5)*num*num)
    print(round(area,2))
