"""
Input Description:
A positive integer is provided as an input.

Output Description:
Print the factorial of the integer.

Sample Input :
2
Sample Output :
2
"""

num = input("")
num = int(num)
fact = 1
if num<0:
    print("Error")
elif num==0:
    fact = 1
    print(fact)
else:
    while num>1:
        fact = fact*num
        num = num - 1
    print(fact)