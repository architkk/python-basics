"""
Input Description:
A single line containing an integer.

Output Description:
Print the sum of the digits of the integer.

Sample Input :
124
Sample Output :
7
"""

num = int(input(""))
sum = 0
while(num!=0):
    dig = num%10
    sum = sum+dig
    num = int(num/10)
print(sum)
