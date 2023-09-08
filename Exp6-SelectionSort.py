l=[]
n=int(input("enter n"))
for i in range(n):
	a=int(input())
	l.append(a)
for i in range(n):
	for j in range(i+1,n,1):
		if l[i]>l[j]:
			c=l[i]
			l[i]=l[j]
			l[j]=c
print(l)
