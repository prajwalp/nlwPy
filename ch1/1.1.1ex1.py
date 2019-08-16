#1.1.1 Example 1

n0 = int(input('Enter the starting number: '))
t = int(input('Enter the number of iterations: '))

#n0 = 998123456789
#t = 350

l=[]
l.append(n0)
e=0
for i in range(t):
	if(int(str(int(n0))[-1])%2 == 0):
		n0 = n0/2
	else:
		n0 = 3*n0 + 1
	if(e==0 and n0 in l):
		e = 1
	l.append(n0)
	print(n0)
if (e==1):
	print('The starting point is eventually periodic')
