#1.1.1 Example 2: Logistic Map trajectory

import fractions as fr
import math

#Logistic Map
def f(x):
	return 4*x*(1-x)

check = int(input('Enter 1 for fractional mode or 2 for float mode: '))

if(check == 1):
	#Allowing for fractional input since number is between 0 and 1
	num = int(input('Enter numerator of starting point: '))
	den = int(input('Enter denominator of starting point: '))
	y0 = fr.Fraction(num,den)
	y=y0
else:
	y0 = float(input('Enter the starting point: '))
	y=float(y0)

t = int(input('Enter the number of iterations: '))

for i in range(t):
	y = f(y)
	print(float(y))

#Error between analytical and numerical value
x_true = 0.5 - 0.5 * math.cos(2**t * math.acos(1-2*y0))
err = x_true - y

print('Error between exact and numerical value: ',err)

