def green(n):
	return lambda a:a*n
k=int(input("enter k"))
x=green(k)
print(x(10))
z=lambda a,b,c: a+b+c
print(z(5,6,7))
