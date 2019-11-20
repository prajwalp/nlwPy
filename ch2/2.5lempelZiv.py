#Lempel and Ziv complexity

s1=input('Enter the string: ')
n=len(s1)
s=[int(i) for i in s1]

C=1
i=0
j=0
while(i+j<n):
	for j in range(i,n):
		if(s1[i:j+1] not in s1[:j]):
			C+=1
			i=j
			break
	i=i+1
print('Complexity:',C)

