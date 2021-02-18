"""
Input Description:
Three values are given to you as the input. these values correspond to Principle amount, Interest Rate and Time in that particular order.

Output Description:
Find the Simple interest and print it up to two decimal places. Round off if required.

Sample Input :
1000 2 5
Sample Output :
100.00
"""

p,r,t = input("").split()
p = float(p)
r = float(r)
t = float(t)

si = (p*t*r)/100
print(format(si, '.2f'))
