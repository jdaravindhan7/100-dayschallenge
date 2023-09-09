n=int(input())
l=[]
se=int(input("enter search element"))
for i in range(n):
	a=int(input())
	l.append(a)
v=n-1
u=0
c=0
for i in range(n):
	mid=int((u+v)/2)
	if se==l[mid]:
		c+=1
		break
	elif se>l[mid]:
		u=mid
	elif se<mid:
		v=mid
if c==1:
	print("element found")
else:
	print("element not found")
