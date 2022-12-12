'''
DATE:12TH NOV 2022
DAY: MONDAY
TOPIC: NUMBER SYSTEM
AUTHOR: RAMA BHARGAVI
'''
from decimal import Decimal as d
h=d(0.7+0.2)
print(h) # will give exact lengthy answer 0.8999999999999999111821580----
h=d(0.7)+d(0.2)
print(h) #will get exact half answer 0.8999999999999999666933092612
h=d('0.7')+d('0.2')
print(h) #0.9
a=5.2;b=3.2
c=a+b
print(c) #8.4
print('%.1f' %c) #8.4
# print(7/0) #zeroDivisionError: division by zero
print(1/1) #1.0
from fractions import Fraction as f
# h=f(1,0) #ZeroDivisionError: fraction(1,0)
d=f(1,1)
print(d) #1
k=f(0,3)
print(k) #0
g=f(5,40)
print(g) #1/8
q=1_23
print(q,type(q)) #123 int
f=1_2.3
print(f,type(f)) #12.3 float
# k=1_.3 #SyntaxError:invalid decimal literal 
# n=1._3 #SyntaxError: invalid decimal literal