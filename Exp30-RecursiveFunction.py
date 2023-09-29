def drama(n):
	if(n>0):
		result=n+drama(n-1)
		print(result)
	else:
		result=0
	return result
n=int(input("enter n"))
drama(n)
