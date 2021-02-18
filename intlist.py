"""
Input Description:
A single line contains an integer N.

Output Description:
Print the values from 1 to N in a separate line.

Sample Input :
5
Sample Output :
1
2
3
4
5
"""

num = input("")
num = int(num)
if num<=0:
    print("ERROR")
else:
    for i in range(num):
        a = i+1
        print(a)
