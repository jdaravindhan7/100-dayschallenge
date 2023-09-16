a=[]
b=[]
n=int(input('enter n'))
print('enter list elements')
for i in range(0,n):
	c=int(input())
	a.append(c)
for i in range(0,n):
	c=int(input())
	b.append(c)
a.extend(b)
print(a)
