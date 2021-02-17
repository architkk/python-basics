"""
Input Description:
A number is provided in Celcius as the input of the program.

Output Description:
The output shall be the temperature converted into Fahrenheit corresponding to the input value print up to two decimal places and round off if required.

Sample Input :
12
Sample Output :
53.60
"""

temp = input("")
temp = float(temp)
temp_fh = (temp*9/5)+32
print(round(temp_fh, 2)) #Rounding off to 2 decimal places