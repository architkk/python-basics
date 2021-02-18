"""
Input Description:
The Radius of a circle is provided as the input of the program.

Output Description:
Calculate and print the Circumference of the circle corresponding to the input radius up to two decimal places.

Sample Input :
2
Sample Output :
12.57
"""

import math

num = float(input(""))
if num<0:
    print("ERROR")
else:
    c = 2*math.pi*num
    print(round(c,2))