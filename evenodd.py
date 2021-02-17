"""
Input Description:
A number is provided as the input.

Output Description:
Find out whether the number is odd or even. Print "Odd" or "Even" for the corresponding cases. Note: In case of a decimal, Round off to nearest integer and then find the output. In case the input is zero, print "Zero".

Sample Input :
2
Sample Output :
Even12.6
"""

num = input("")
num = float(num)
num = int(num)
rem = num%2
if num==0:
    print("Zero")
else:
    if rem==1:
        print("Odd")
    else:
        print("Even")