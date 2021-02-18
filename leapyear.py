"""
Input Description:
A Year is the input in the form of a positive integer.

Output Description:
Print "Y" if its a leap year and "N" if its a common year.

Sample Input :
2020
Sample Output :
Y
"""

num = input("")
num = int(num)
if num<=0:
    print("ERROR")
else:
    rem = num%4
    if rem==0:
        print("Y")
    else:
        print("N")
