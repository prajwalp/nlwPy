#time comparision
import matplotlib.pyplot as plt
import math
import time

#number of points to be sampled

#defining the function to be transformed
def f(t):
	return math.cos(2*math.pi*t/N)

def DFT(N):
	#real and imaginary parts of the transform
	realPart=[]
	imPart=[]


	f_w=[]
	#matrix multiplication of DFT
	for i in range(N):
		tempR=0
		tempI=0
		for j in range(N):
			tempR+=math.cos(2*math.pi*i*j/N)*f(j)/N
			tempI-=math.sin(2*math.pi*i*j/N)*f(j)/N
		realPart.append(tempR)
		imPart.append(tempI)


timeTaken=[]
nVal=[]
for x in range(1,200):
	N=x
	nVal.append(N)
	t0=time.time()
	DFT(N)
	timeTaken.append(time.time()-t0)
plt.plot(nVal,timeTaken)
plt.xlabel('N values')
plt.ylabel('Time taken for DFT')
plt.show()