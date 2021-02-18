"""
Input Description:
A single line contains an integer N.

Output Description:
Print the digits of the integer in a single line separated by space,

Sample Input :
348
Sample Output :
3 4 8
"""

num = int(input(""))
dig = []
if num>0:
    while num!=0:
        dig.append(num%10)
        num = int(num/10)
    dig.reverse()
    print(' '.join(map(str, dig)))
elif num==0:
    print(0)
else:
    num = -1*num
    while num!=0:
        dig.append(num%10)
        num = int(num/10)
    dig.append("-")
    dig.reverse()
    print(' '.join(map(str, dig)))


