"""
Input Description:
You are provided with two numbers as input.

Output Description:
Print the small number out of the two numbers.

Sample Input :
23 1
Sample Output :
1
"""

num1, num2 = input("").split() #taking 2 inputs at same time
num1 = float(num1)
num2 = float(num2)
arr = [num1,num2]
print(min(arr))