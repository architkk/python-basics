"""
Input Description:
A string is provide as an input

Output Description:
Remove all the whitespaces and then print the length of the remaining string.

Sample Input :
Lorem Ipsum
Sample Output :
10
"""

string = input("")
string = string.replace(" ", "") #Removing white spaces
print(len(string)) #String Length