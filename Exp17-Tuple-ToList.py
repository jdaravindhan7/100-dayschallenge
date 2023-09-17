a=()
b=list(a)
n=int(input("enter n"))
for i in range(n):
	c=int(input())
	b.append(c)
print(b)
a=tuple(b)
print(a)
