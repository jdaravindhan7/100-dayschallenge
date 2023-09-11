
n=int(input("enter n"))
for h in range(n):
	for k in range(1,n+1):
		for i in range(n,k,-1):
			print(" ",end=" ")
		for j in range(0,k):
			print("*",end=" ")
			print(" ",end=" ")
		print()
	for k in range(1,n):
		for i in range(0,k):
			print(" ",end=" ")
		for j in range(n,k,-1):
			print("*",end=" ")
			print(" ",end=" ")
		print()
	
