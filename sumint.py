"""
Input Description:
A single line contains an integer N.

Output Description:
Print the sum of values from 1 to N.

Sample Input :
10
Sample Output :
55
"""

num = int(input(""))
if num<=0:
    print("ERROR")
else:
    sum = num*(num+1)/2
    sum = int(sum)
    print(sum)