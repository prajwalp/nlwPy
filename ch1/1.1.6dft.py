#Non numpy implementation
import matplotlib.pyplot as plt
import math

#number of points to be sampled
N=2**3
#defining the function to be transformed
def f(t):
	return math.cos(2*math.pi*t/N)

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

T=list(range(N))
plt.plot(T,realPart,'bo',markersize=4,alpha=0.5,label='Real Part')
plt.plot(T,imPart,'rx',markersize=4,alpha=0.5,label='imaginary Part')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Fourier Transform Values')
plt.show()

