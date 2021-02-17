"""
Input Description:
The input is in the form of a number.

Output Description:
Find the days in the month corresponding to the input number. Print Error if the input is not in a valid range.

Sample Input :
8
Sample Output :
31
"""

num = input("")
num = int(num)
montday = {"1":"31",
           "2":"28",
           "3":"31",
           "4":"30",
           "5":"31",
           "6":"30",
           "7":"31",
           "8":"31",
           "9":"30",
           "10":"31",
           "11":"30",
           "12":"31"} #Making a dictionary
if num==0:
    print("Error")
else:
    if num>12:
        print("Error")
    else:
        num = str(num)
        print(montday[num])