"""
Input Description:
A single line containing an integer.

Output Description:
Print the even and odd integers of the integer in a separate line.

Sample Input :
1234
Sample Output :
2 4
1 3
"""

num = input("")
num = int(num)
even = []
odd = []
while (num!=0):
    dig = num%10
    if dig%2 == 0:
        even.append(dig)
    else:
        odd.append(dig)
    num = int(num/10)
even.reverse()
odd.reverse()
even.sort(reverse=False) # Arranging list in assending order
odd.sort(reverse=False)
print(' '.join(map(str, even)))
print(' '.join(map(str, odd)))
