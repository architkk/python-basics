"""
Input Description:
A single line containing 2 integers separated by space.

Output Description:
Print the HCF of the integers.

Sample Input :
2 3
Sample Output :
1
"""

x,y = input("").split()
x = int(x)
y = int(y)
if x==0 or y==0:
    print(0)
else:
    if x>y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if (x%i == 0) and (y%i == 0):
            hcf=i
    print(hcf)

