#Example 3: Bernoulli map trajectory

import fractions as fr
import math

def f(x):
	if(x<0.5):
		return 2*x
	else:
		return 2*x - 1

check = int(input('Enter 1 for fractional mode or 2 for float mode: '))

if(check == 1):
	num = int(input('Enter numerator of starting point: '))
	den = int(input('Enter denominator of starting point: '))
	y0 = fr.Fraction(num,den)
	y=y0
else:
	y0 = float(input('Enter the starting point: '))
	y=float(y0)

t = int(input('Enter the number of iterations: '))

l=[]
l.append(y)
e=0

for i in range(t):
	y = f(y)
	if(e==0 and y in l):
		e = 1
	l.append(y)
	print(float(y))

if (e==1):
	print('The starting point is eventually periodic')

