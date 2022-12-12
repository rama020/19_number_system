'''
DATE:12TH NOV 2022
DAY: MONDAY
TOPIC: NUMBER SYSTEM
AUTHOR: RAMA BHARGAVI
'''
a=3;b=0.6
print(isinstance(a,int)) #True
print(isinstance(b,int)) #False
j=4j
print(j,type(j)) #4j complex
from fractions import Fraction as F
print(F(6,3)) #2
print(F(2.3)) #2
print(F('2.3')) #23/10
print(F("2.3")) #23/10
f=5*3.2j
print(f,type(f)) #16j compex
print(f.real) #0.0
print(f.imag) #16.0
print(1e0) #1.0
print(2e1) #20.0
