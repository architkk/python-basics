"""
Input Description:
A single line contains an integer N.

Output Description:
Print the even values from 1 to N in a separate line.

Sample Input :
6
Sample Output :
2
4
6
"""

num = int(input(""))
i=0
if num<=0:
    print("ERROR")
else:
    if num%2==0:
        while(num!=i):
            i = i+2
            print(i)
    else:
        num = num-1
        while (num!=i):
            i = i + 2
            print(i)