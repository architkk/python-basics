"""
Input Description:
A positive integer is provided to you as an input.

Output Description:
Print the First 3 multiples of the number with single spaces between them as an output.

Sample Input :
2
Sample Output :
2 4 6
"""

num = input("")
num = int(num)
if num<0:
    print("Error")
else:
    num1 = num
    num2 = 2*num
    num3 = 3*num
    #print(num1, num2, num3)
    #OR
    arr = [num1, num2, num3]
    for i in range(3): #changes i from 0 to 2
        print(arr[i], end=" ") #Prints in the same line with space


