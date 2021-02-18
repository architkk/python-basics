"""
Input Description:
First line contains an integer A. Second line contains an Integer N.

Output Description:
Print the integer A, N times in a separate line.

Sample Input :
2 3
Sample Output :
2
2
2
"""

a,n=input("").split()
a = int(a)
n = int(n)
if n==0:
    print(a)
else:
    for i in range(n):
        print(a)
