n=int(input("enter number"))
temp=n
sum=0
while temp>0:
	digit=temp%10
	sum+=digit**3
	temp=temp//10
if(n==sum):
	print("it is a amstrong number")
else:
	print("not a amstrong number")

