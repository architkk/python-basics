"""
Input Description:
A positive integer is provided as an input.

Output Description:
Print the table of nine with single space between the elements till the number that is input.

Sample Input :
3
Sample Output :
9 18 27
"""

num = input("")
num = int(num)
if num<0:
    print("ERROR")
elif num==0:
    print("NULL")
else:
    arr = [] #Empty Array
    for i in range(num):
        arr.append(9*(i+1))
    # print(' '.join(map(str, arr))) #Printing elements of array with spaces
    for i in range(num):
        print(arr[i], end=" ")